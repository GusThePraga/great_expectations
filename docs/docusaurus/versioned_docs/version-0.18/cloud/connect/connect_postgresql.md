---
sidebar_label: 'Connect GX Cloud to PostgreSQL'
title: 'Connect GX Cloud to PostgreSQL'
description: Connect GX Cloud to a PostgreSQL Data Source.
---

import TabItem from '@theme/TabItem';
import Tabs from '@theme/Tabs';

To validate data stored in a PostgreSQL database from GX Cloud, you must add the GX Agent to your deployment environment. The GX Agent acts as an intermediary between GX Cloud and PostgreSQL and allows you to securely access and validate your data in GX Cloud.

## Prerequisites

- You have a [GX Cloud account](https://greatexpectations.io/cloud) with [Admin or Editor permissions](../about_gx.md#roles-and-responsibilities).

- You have deployed the GX Agent. See [Deploy the GX Agent](../deploy_gx_agent.md).

- You have a PostgreSQL database, schema, and table.

- To improve data security, GX recommends creating a separate PostgreSQL user for your GX Cloud connection.

- [pgAdmin (optional)](https://www.pgadmin.org/download/)

- You have stopped all local running instances of the GX Agent.

## Connect to a PostgreSQL Data Asset

1. In GX Cloud, click **Data Assets** > **New Data Asset** > **PostgreSQL**.

2. Copy the code in the code pane.

3. Prepare your PostgreSQL environment:

   - In pgAdmin, select a database.

   - Click **Tools** > **Query Tool**.

   - Paste the code you copied in step 2 into the **Query** pane to create and assign the `gx_role` role and allow GX Cloud to access to all `public` schemas and tables on a specific database.

      Replace `<your_password>` and `<your_database>` with your own values. `ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT ON TABLES TO gx_role;` is optional and gives the `gx_role` user access to all future tables in the defined schema.

    - Click **Execute/Refresh**.

4. In GX Cloud, click **I have created a GX Cloud user with valid permissions** and then click **Continue**.

5. Enter a meaningful name for the Data Source in the **Data Source name** field.

6. Enter a connection string in the **Connection string** field. The connection string format is `postgresql+psycopg2//YourUserName:YourPassword@YourHostname:5432/YourDatabaseName`. 

7. Optional. Select **Test connection** to test the Data Source connection. Testing the connection to the Data Source is a preventative measure that makes sure the connection configuration is correct. This verification can help you avoid errors and can reduce troubleshooting downtime.

8. Click **Continue**.

9. Select **Table Asset** or **Query Asset** and complete the following fields:

    - **Table name**: When **Table Asset** is selected, enter the name of the Data Source table you're connecting to.
    
    - **Data Asset name**: Enter a name for the Data Asset. Data Asset names must be unique across all Data Sources in GX Cloud.

    - **Query**: When **Query Asset** is selected, enter the query that you want to run on the Data Asset. 

10. Select the **Complete Asset** tab to provide all Data Asset records to your Expectations and validations, or select the **Batches** tab to use subsets of Data Asset records for your Expectations and validations. If you selected the **Batches** tab, complete the following fields:

    - **Split Data Asset by** - Select **Year** to partition Data Asset records by year, select **Year - Month** to partition Data Asset records by year and month, or select **Year - Month - Day** to partition Data Asset records by year, month, and day.

    - **Column of datetime type** - Enter the name of the column containing the date and time data.

11. Optional. Select **Add Data Asset** to add additional tables or queries and repeat steps 8 and 9.

12. Click **Finish**.

13. Create an Expectation. See [Create an Expectation](/cloud/expectations/manage_expectations.md#create-an-expectation).
