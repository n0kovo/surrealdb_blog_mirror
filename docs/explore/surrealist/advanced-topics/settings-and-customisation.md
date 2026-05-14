---
position: 6
title: Settings and customisation
description: Tune Surrealist with behaviour and editor options, appearance and default result modes, connection templates, local database serving paths, and experimental feature flags.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/explore/surrealist/advanced-topics/settings-and-customisation.mdx"
---

# Settings and customisation

In the bottom left of the interface you can find a settings button (⚙) to open the settings dialog. These settings allow you to further customise the behaviour and appearance of Surrealist, such as switching between light and dark mode, increasing or decreasing the editor font sizes, and configure default values for new connections.

## Behaviour

In this section you can configure the behaviour of the interface, such as connection and editor related settings.

## Appearance

The appearance section allows you to scale the fonts in the editor and also select your default query output view and set the behaviour for your Query and designer views.

## Templates

You can configure [connection templates](connection-templates.md) to reuse connection details when creating new connections. This is especially useful when you find yourself connecting to similar databases frequently.

## Database serving

This section allows you to alter the behaviour of the database serving functionality found in Surrealist Desktop, such as altering the port and specifying the path to the database executable.

## Feature flags

Feature flags allow you to enable or disable stable and experimental features in Surrealist to suit your needs best.

Some of these features may not be stable and may not work as expected or be removed in future versions. To access the feature flags, press `Ctrl + K` or `Cmd + K` on your keyboard to open the command palette, then type in "Manage Feature Flags" and hit enter. You'll be taken to the feature flags settings.

After enabling a feature flag, you can access it by clicking on the settings button in the bottom left of the interface and selecting the feature flags tab. Here, you can enable or disable features. Here is a list of the current feature flags:

<table>
    <thead>
        <tr>
            <th scope="col">Options</th>
            <th scope="col">Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td scope="row" data-label="Type">
                `feature_flags`
            </td>
            <td scope="row" data-label="Description">
                Toggle feature flags.
            </td>
        </tr>
        <tr>
            <td scope="row" data-label="Type">
                `models_view`
            </td>
            <td scope="row" data-label="Description">
                Toggle the view for SurrealML models.
            </td>
        </tr>
        <tr>
            <td scope="row" data-label="Type">
                `apidocs_view`
            </td>
            <td scope="row" data-label="Description">
                Toggle the view for API documentation.
            </td>
        </tr>
        <tr>
            <td scope="row" data-label="Type">
                `themes`
            </td>
            <td scope="row" data-label="Description">
                Toggle between light and dark mode.
            </td>
        </tr>
        <tr>
            <td scope="row" data-label="Type">
                `newsfeed`
            </td>
            <td scope="row" data-label="Description">
                Toggle the newsfeed view.
            </td>
        </tr>
        <tr>
            <td scope="row" data-label="Type">
                `database_version_check`
            </td>
            <td scope="row" data-label="Description">
                Toggle the database version check in the Surrealist CLI
            </td>
        </tr>
        <tr>
            <td scope="row" data-label="Type">
                `highlight_tool`
            </td>
            <td scope="row" data-label="Description">
                Toggle the highlight tool.
            </td>
        </tr>
        <tr>
            <td scope="row" data-label="Type">
                `surreal_compat`
            </td>
            <td scope="row" data-label="Description">
                Toggle SurrealDB version between `1.x` and `2.x`.
            </td>
        </tr>
        <tr>
            <td scope="row" data-label="Type">
                `changelog`
            </td>
            <td scope="row" data-label="Description">
                Toggle the changelog view to see the latest changes, read all or unread all.
            </td>
        </tr>
    </tbody>
</table>
