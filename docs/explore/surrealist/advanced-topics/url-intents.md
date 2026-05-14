---
position: 4
title: URL intents
description: "Trigger Surrealist actions from URLs via intent query parameters on app.surrealdb.com, surrealist:// deep links on desktop, argument syntax, and other supported intents."
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/explore/surrealist/advanced-topics/url-intents.mdx"
---

# URL intents

Surrealist provides a low-level system for triggering actions within the interface through a URL. For example, you can use it to open specific dialogs, switch views, or even run queries.
The intent system is used under the hood to power the command palette so most commands found there can be triggered via intents.

## Usage

Intents can be configured using the `intent` query argument. A simple example of an intent to open the connections dialog would look like this:

```
https://app.surrealdb.com/?intent=open-connections
```

A more advanced example of an intent can contain additional arguments. These are key-value pairs separated by `=` and are appended after the intent name suffixed by a colon `:`.
This is an example of an intent to open the settings page and switch to the appearance tab:

```
https://app.surrealdb.com/?intent=open-settings:tab=appearance
```

You can also trigger intents for the Desktop App by using the Surrealist URI protocol. This will open a new Surrealist window
if one is not already open. Here is an example of an intent to toggle database serving:

```
surrealist://?intent=toggle-serving
```

Additionally, certain intents are bound to a specific view. In this case Surrealist will automatically switch to the correct view when the intent is triggered.

## List of intents

  

  

<table>
    <thead>
        <tr>
            <th scope="col">Name</th>
            <th scope="col">View</th>
            <th scope="col">Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td scope="row" data-label="Type">
                `open-command-palette`
            </td>
			<td scope="row" data-label="View">
                &hyphen;
            </td>
            <td scope="row" data-label="Description">
                Open the command palette dialog.
            </td>
        </tr>
		<tr>
			<td scope="row" data-label="Type">
				`open-connections`
			</td>
			<td scope="row" data-label="View">
				&hyphen;
			</td>
			<td scope="row" data-label="Description">
				Open the connection list dialog.
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Type">
				`open-help`
			</td>
			<td scope="row" data-label="View">
				&hyphen;
			</td>
			<td scope="row" data-label="Description">
				Open the help and support dialog.
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Type">
				`open-news`
			</td>
			<td scope="row" data-label="View">
				&hyphen;
			</td>
			<td scope="row" data-label="Description">
				Opens the news drawer.
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Type">
				`open-changelog`
			</td>
			<td scope="row" data-label="View">
				&hyphen;
			</td>
			<td scope="row" data-label="Description">
				Opens the changelog dialog.
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Type">
				`open-settings`
			</td>
			<td scope="row" data-label="View">
				&hyphen;
			</td>
			<td scope="row" data-label="Description">
				Opens the settings dialog. You can specify a tab to open using the `tab` argument.
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Type">
				`open-embedder`
			</td>
			<td scope="row" data-label="View">
				&hyphen;
			</td>
			<td scope="row" data-label="Description">
				Opens the embedder dialog.
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Type">
				`open-desktop-download`
			</td>
			<td scope="row" data-label="View">
				&hyphen;
			</td>
			<td scope="row" data-label="Description">
				Opens the Surrealist Desktop download dialog. Only applicable to the web app.
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Type">
				`open-keymap`
			</td>
			<td scope="row" data-label="View">
				&hyphen;
			</td>
			<td scope="row" data-label="Description">
				Opens the keymap dialog.
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Type">
				`new-connection`
			</td>
			<td scope="row" data-label="View">
				&hyphen;
			</td>
			<td scope="row" data-label="Description">
				Opens the connection creator.
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Type">
				`new-table`
			</td>
			<td scope="row" data-label="View">
				&hyphen;
			</td>
			<td scope="row" data-label="Description">
				Opens the table creator.
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Type">
				`toggle-serving`
			</td>
			<td scope="row" data-label="View">
				&hyphen;
			</td>
			<td scope="row" data-label="Description">
				Toggles database serving. Only applicable to the desktop app.
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Type">
				`open-serving-console`
			</td>
			<td scope="row" data-label="View">
				&hyphen;
			</td>
			<td scope="row" data-label="Description">
				Reveals the database serving console drawer. Only applicable to the desktop app.
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Type">
				`increase-window-scale`
			</td>
			<td scope="row" data-label="View">
				&hyphen;
			</td>
			<td scope="row" data-label="Description">
				Increases the window zoom level. Only applicable to the desktop app.
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Type">
				`decrease-window-scale`
			</td>
			<td scope="row" data-label="View">
				&hyphen;
			</td>
			<td scope="row" data-label="Description">
				Decreases the window zoom level. Only applicable to the desktop app.
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Type">
				`increase-editor-scale`
			</td>
			<td scope="row" data-label="View">
				&hyphen;
			</td>
			<td scope="row" data-label="Description">
				Increases the font size of text editors.
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Type">
				`decrease-editor-scale`
			</td>
			<td scope="row" data-label="View">
				&hyphen;
			</td>
			<td scope="row" data-label="Description">
				Decreases the font size of text editors.
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Type">
				`toggle-pinned`
			</td>
			<td scope="row" data-label="View">
				&hyphen;
			</td>
			<td scope="row" data-label="Description">
				Toggle whether the window is always on top. Only applicable to the desktop app.
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Type">
				`highlight-tool`
			</td>
			<td scope="row" data-label="View">
				&hyphen;
			</td>
			<td scope="row" data-label="Description">
				Opens a developer tool used to generate clipboard compatible SurrealQL highlighting
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Type">
				`new-query`
			</td>
			<td scope="row" data-label="View">
				Query
			</td>
			<td scope="row" data-label="Description">
				Creates a new query tab.
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Type">
				`run-query`
			</td>
			<td scope="row" data-label="View">
				Query
			</td>
			<td scope="row" data-label="Description">
				Executes the current query
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Type">
				`save-query`
			</td>
			<td scope="row" data-label="View">
				Query
			</td>
			<td scope="row" data-label="Description">
				Open the query save dialog for the active query
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Type">
				`format-query`
			</td>
			<td scope="row" data-label="View">
				Query
			</td>
			<td scope="row" data-label="Description">
				Formats the current query
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Type">
				`toggle-variables`
			</td>
			<td scope="row" data-label="View">
				Query
			</td>
			<td scope="row" data-label="Description">
				Toggles the visibility of the variables panel
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Type">
				`infer-variables`
			</td>
			<td scope="row" data-label="View">
				Query
			</td>
			<td scope="row" data-label="Description">
				Infer variables from the currently active query
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Type">
				`open-saved-queries`
			</td>
			<td scope="row" data-label="View">
				Query
			</td>
			<td scope="row" data-label="Description">
				Opens the saved queries drawer
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Type">
				`open-query-history`
			</td>
			<td scope="row" data-label="View">
				Query
			</td>
			<td scope="row" data-label="Description">
				Opens the query history drawer
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Type">
				`explore-table`
			</td>
			<td scope="row" data-label="View">
				Explorer
			</td>
			<td scope="row" data-label="Description">
				Opens a table in the Explorer view. Requires a `table` argument with the table name.
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Type">
				`import-database`
			</td>
			<td scope="row" data-label="View">
				Explorer
			</td>
			<td scope="row" data-label="Description">
				Opens the data importing dialog.
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Type">
				`export-database`
			</td>
			<td scope="row" data-label="View">
				Explorer
			</td>
			<td scope="row" data-label="Description">
				Opens the data exporting dialog.
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Type">
				`design-table`
			</td>
			<td scope="row" data-label="View">
				Designer
			</td>
			<td scope="row" data-label="Description">
				Opens a table in the Designer view. Requires a `table` argument with the table name.
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Type">
				`create-user`
			</td>
			<td scope="row" data-label="View">
				Authentication
			</td>
			<td scope="row" data-label="Description">
				Opens the user creation dialog. Requires a `level` argument set to either ROOT, NAMESPACE, or DATABASE.
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Type">
				`create-scope`
			</td>
			<td scope="row" data-label="View">
				Authentication
			</td>
			<td scope="row" data-label="Description">
				Opens the scope creation dialog.
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Type">
				`register-user`
			</td>
			<td scope="row" data-label="View">
				Authentication
			</td>
			<td scope="row" data-label="Description">
				Opens the scope user registration dialog. Requires a `scope` argument with the scope name.
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Type">
				`docs-switch-language`
			</td>
			<td scope="row" data-label="View">
				API Docs
			</td>
			<td scope="row" data-label="Description">
				Changes the language used for the code snippets. Requires a `lang` argument with a valid language code.
			</td>
		</tr>
	</tbody>
</table>
