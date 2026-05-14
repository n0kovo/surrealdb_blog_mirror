---
title: "What is SurrealML: A getting started guide"
slug: "what-is-surrealml-a-getting-started-guide"
date: "2023-12-12T00:00:00.000Z"
categories:
  - "tutorials"
  - "engineering"
read_time: "9 min read"
summary: "The developer community has made great strides in building open-source machine-learning packages that save machine-learning models. However, there are still areas of this pipeline that are not fully complete."
source: "https://surrealdb.com/blog/what-is-surrealml-a-getting-started-guide"
cover: "../../assets/5882bfcb7fdecab0.jpg"
---

# What is SurrealML: A getting started guide

![What is SurrealML: A getting started guide](../../assets/5882bfcb7fdecab0.jpg)

## Introduction

The developer community has made great strides in building open-source machine-learning packages that save machine-learning models. However, there are still areas of this pipeline that are not fully complete. The problems of hosting and version control of machine learning models are very real. How do you store your models? How do you deploy those models? How do you roll over to a new version and compare the performance of those two models? While a lot of tools can carry out these individual steps, they generally require custom-built pipelines and systems. We can read more on these challenges [here](https://medium.com/@rohitshende020/how-to-overcome-common-challenges-in-deploying-machine-learning-models-d7f753a381a7).

Unlike the training of models, hosting and version control of models is not as simple as importing a library and running a few commands.

This is where [SurrealML](/features) comes in. SurrealML does not aim to train models. There a plenty of mature libraries with teams of very smart people working on them doing that. Instead, SurrealML is a package that enables users to package a trained machine learning model, deploy it onto their SurrealDB instance, and then perform ML inference on the deployed model through SurrealQL statements, all in just a few short commands!

Since the user can interact with the deployed model via SurrealQL, implementing the model inference is very flexible. For instance, you can have two different versions of the same model. In your SurrealQL command, you can feed columns into both versions and store or return the results. A data scientist can merely run an SurrealQL query against data in the database between two different versions of the same model to compare the differences. Users can even feed the outcomes of the models into other parameters of the search. Remember, SurrealQL is a language. There is nothing stopping a user from filtering results in a table by passing in columns of a table into a deployed model and filtering the rows based on an output of the deployed model for that row.

As a quick demonstration of this power, we have the following query:

```surrealql
CREATE house_listing SET squarefoot_col = 500.0, num_floors_col = 1.0;
CREATE house_listing SET squarefoot_col = 1000.0, num_floors_col = 2.0;
CREATE house_listing SET squarefoot_col = 1500.0, num_floors_col = 3.0;

SELECT * FROM (
    SELECT
      *,
      ml::house-price-prediction<0.0.1>({
        squarefoot: squarefoot_col,
        num_floors: num_floors_col
      }) AS price_prediction
    FROM house_listing
  )
  WHERE price_prediction > 177206.21875;
```

What is happening here is that we are feeding the columns from a the table `house_listing` into a model we uploaded called `house-price-prediction` with a version of `0.0.1`. We then get the results of that trained ML model as the column `price_prediction`. We then use the calculated predictions to filter the rows giving us the following result:

```json
[
    {
        "id": "house_listing:7bo0f35tl4hpx5bymq5d",
        "num_floors_col": 3,
        "price_prediction": 406534.75,
        "squarefoot_col": 1500
    },
    {
        "id": "house_listing:8k2ttvhp2vh8v7skwyie",
        "num_floors_col": 2,
        "price_prediction": 291870.5,
        "squarefoot_col": 1000
    }
]
```

With this detour we can see how easy it would be to retroactively see how a new model would perform on existing data. It would be simple to have two model versions in our query to compare the difference.

Looking at what you can do with SurrealML, you can deploy your model with a few lines of code, and then write customisable processes interacting with all deployed models at your fingertips with just one line of SurrealQL. We’ll show you how to try this out in this blog, and the first step is to set up our environment.

## Prerequisites and Environment Setup

To upload a model and run ML queries we need the following checklist:

- [ ] a client for packaging trained machine learning models so they can be uploaded to SurrealDB
- [ ] a client to interact with SurrealDB
- [ ] a ML framework to train the model

### Packaging trained ML models

If you want to package ML models, you will need Python, and you will also need to install the SurrealML Python package which is housed in the following repo:

[https://github.com/surrealdb/surrealml](https://github.com/surrealdb/surrealml)

### Client for SurrealQL queries

We can perform SurrealQL statements against SurrealDB in a range of languages. However, considering that we are using Python to train and package our ML models, it makes sense that we are also going to use Python to perform the SurrealQL operations so we can have everything running in one script. The Python client is housed in the repo below:

[https://github.com/surrealdb/surrealdb.py](https://github.com/surrealdb/surrealdb.py)

### ML framework for training models

We also need to train our ML model. For this example, we will be covering `sklearn` and `pytorch` examples, so install the ML module that you wish to use. Now that we have everything set up the way we want it, we can move on to training our models.

## Training our Pytorch model

For our `pytorch` example, we will use `numpy` to handle the data. For our toy example, we will do a simple linear regression model to predict the house prices of a simple small dataset. This is a classic example of exploring machine learning. First, we define our data with the following code:

```python





squarefoot = np.array([1000, 1200, 1500, 1800, 2000, 2200, 2500, 2800, 3000, 3200], dtype=np.float32)
num_floors = np.array([1, 1, 1.5, 1.5, 2, 2, 2.5, 2.5, 3, 3], dtype=np.float32)
house_price = np.array([200000, 230000, 280000, 320000, 350000, 380000, 420000, 470000, 500000, 520000], dtype=np.float32)
```

We then get the parameters to perform normalisation to get better convergence with the code below:

```python
squarefoot_mean = squarefoot.mean()
squarefoot_std = squarefoot.std()
num_floors_mean = num_floors.mean()
num_floors_std = num_floors.std()
house_price_mean = house_price.mean()
house_price_std = house_price.std()
```

We then normalise our data with the following code:

```python
squarefoot = (squarefoot - squarefoot.mean()) / squarefoot.std()
num_floors = (num_floors - num_floors.mean()) / num_floors.std()
house_price = (house_price - house_price.mean()) / house_price.std()
```

We then create our tensors so they can be loaded into our model and stack them together with the code below:

```python
squarefoot_tensor = torch.from_numpy(squarefoot)
num_floors_tensor = torch.from_numpy(num_floors)
house_price_tensor = torch.from_numpy(house_price)

X = torch.stack([squarefoot_tensor, num_floors_tensor], dim=1)
```

We are now at the stage where we can define our linear regression model. To avoid bloat of this guide, we are not going to cover the pytorch code in detail as the aim of this guide is to focus on how to use SurrealML. Our Linear regression pytorch model takes the following form:

```python
# Define the linear regression model
class LinearRegressionModel(nn.Module):
    def __init__(self):
        super(LinearRegressionModel, self).__init__()
        self.linear = nn.Linear(2, 1)  # 2 input features, 1 output

    def forward(self, x):
        return self.linear(x)

# Initialize the model
model = LinearRegressionModel()

# Define the loss function and optimizer
criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)
```

We are now ready to train our model on the data we have generated with 100 epochs with the following loop:

```python
num_epochs = 1000
for epoch in range(num_epochs):
    # Forward pass
    y_pred = model(X)

    # Compute the loss
    loss = criterion(y_pred.squeeze(), house_price_tensor)

    # Backward pass and optimization
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    # Print the progress
    if (epoch + 1) % 100 == 0:
        print(f"Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}")
```

Our model is now trained, and we can move on to saving it.

## Saving the Pytorch model with SurrealML

We will use the SurrealML package to store our trained model. However, before we do that we need to create some dummy data so the model can be traced so the model can be saved in the ONNX format making the model language agnostic. We can create the dummy data with the code below:

```python
test_squarefoot = torch.tensor([2800, 3200], dtype=torch.float32)
test_num_floors = torch.tensor([2.5, 3], dtype=torch.float32)
test_inputs = torch.stack([test_squarefoot, test_num_floors], dim=1)
```

We can now wrap our model in the `SurMlFile` object with the following code:

```python
from surrealml import SurMlFile

file = SurMlFile(model=model, name="Prediction", inputs=test_inputs)
```

The name is optional, but the inputs and model are essential. We can now add some metadata to the file, such as our inputs and outputs, with the following code; however, metadata is not essential - it just helps with the buffered compute where we can map column names of an object to the input as seen in our initial SurrealQL example:

```python
file.add_column("squarefoot")
file.add_column("num_floors")
file.add_output("house_price", "z_score", house_price_mean, house_price_std)
```

It must be stressed that the `add_column` order needs to be consistent with the input tensors that the model was trained on. They now act as key bindings to convert dictionary inputs into the model. Also, you should add normalisers for your column.

Good news: these normalisers get arranged automatically, so you don't have to worry about the order you put them in. Remember, using normalisers is not a must - you can also prepare your data yourself.

```python
file.add_normaliser("squarefoot", "z_score", squarefoot_mean, squarefoot_std)
file.add_normaliser("num_floors", "z_score", num_floors_mean, num_floors_std)
```

We then save the model with the following code:

```python
file.save("./test.surml")
```

Before we continue with our Pytorch model, we can make a quick detour for training an sklearn model.

## Training a **scikit-learn** model

If we train either a Pytorch model or a sklearn model, the interfaces will be the same when it comes to loading and interacting with the model. The interactions in the database will also be the same so we will just cover quickly how to train a sklearn model in this section, and then continue with the Pytorch example for the test of the guide.

For our sklearn example, we will train a random forest model with the code below:

```python

from sklearn.ensemble import RandomForestClassifier
from surrealml import SurMlFile

num_classes = 2
X = np.random.rand(100, 28)
y = np.random.randint(num_classes, size=100)

skl_model = RandomForestClassifier(n_estimators=10, max_depth=10)
skl_model.fit(X, y)
test_file = SurMlFile(model=skl_model, name="random forrest classifier", inputs=X, sklearn=True)
test_file.save("./test_forrest.surml")
```

The sklearn model does not require Python to run it, so your sklearn models will run in Rust alongside your Pytorch models in the database and locally. This is achieved because the random forest is essentially transpiled into vectors, which can then be converted into a Pytorch model. Once it’s a Pytorch model, the tracing can be saved in the ONNX format, just like the Pytorch model examples.

We this sklearn detour over, we can now go back to interacting with our Pytorch model locally

## Locally Loading the Model for Inference in Python

If you have a `surml` file, you can load it with the following code:

```python
new_file = SurMlFile.load("./test.surml")
```

Since we’ve previously defined all we need in the headers for normalisation and input mapping, we can now perform our inference with raw computes or buffered computes. A raw compute is what it implies. You have to do all the normalisations and mappings yourself, and you just pass in the raw data. This is to stop us from holding you back if you are doing something fancy with multiple dimension inputs. A raw compute can be performed with the sample code below:

```python
result = new_file.raw_compute([ 1.0, 2.0 ])
```

If we want to do a buffered compute, everything in the header of the file, including the normalisation of the data, will be performed, and we merely need to pass in a [dict](https://docs.python.org/3/library/stdtypes.html#typesmapping) with the correct data mapping as demonstrated with the following code:

```python
result = new_file.buffered_compute({
    "squarefoot": 3200.0,
    "num_floors": 2.0
})
```

And there you have it; you can do inference without having to worry about the metadata around the model or the Python version as the computation is happening in ONNX format with Rust. There is an opportunity for us to add other language bindings in the future to enable these models to run in a variety of languages. All the execution happens in Rust, with Python bindings serving as the interface.

We have now covered all that we need for local inference, we can now move on to deploying our model in SurrealDB and interacting with it.

## Integrating Our Model with SurrealDB

To upload our model into SurrealDB, we can use the `surreal` command-line tool:

```cli
surreal ml import --ns myns --db mydb linear_test.surml
```

It’s that simple. The command-line tool sends the file to the SurrealDB instance which will then store the model for computation when needed.

Now that our model is uploaded onto the SurrealDB instance, we can perform a raw compute with the code below:

```python
outcome = connection.query("ml::Prediction<0.0.1>([ 1.0, 1.0 ]);")
```

Remember, we called our model “Prediction” when packaging our model, but we can call our model whatever we want as SurrealDB supports as many models as you can train and there’s storage space. We can also perform a buffered compute with the following code:

```python
outcome = connection.query("ml::Prediction<0.0.1>({ squarefoot: 500.0, num_floors: 1.0 });")
```

We are just passing in numbers in this example, but remember, this is a raw SQL function, you can be as creative as you want with it.

## Next Steps

SurrealML stands as a game-changer in machine learning, adeptly addressing the complexities of model hosting, version control, and deployment. This guide has taken you through setting up your environment, training models with Pytorch and Sk-Learn, and the intricacies of integrating these models with SurrealDB. SurrealML's marriage of machine learning with SurrealQL's flexibility marks a significant leap in simplifying once cumbersome processes.

But this is just the start.

Join the SurrealDB community on [Discord](https://discord.gg/surrealdb) to dive deeper, exchange ideas, and stay updated with the latest in SurrealML.
