# WHO/WHDH Chart Data Text Summarization - Extracting Insights from Data for Visually Impaired

[WHO's World Health Data Hub(WHDH)](https://data.who.int/home) provides an interactive digital platform and trusted source for global health data, fulfilling WHO’s commitment to provide health data as a public good. The platform brings together an ambitious product stack to deliver an end-to-end solution for WHO data processes. From collection to use the platform provides a world class experience leveraging innovative technology to address challenges and pain points.

![WHO WHDH](https://github.com/microsoft/OpenAI-Hack-Group-5-Humanitarian/blob/main/Images/WHO%20WHDH%20Screen%20Shot.png)

<br />
<br />
<br />

## The Challenge

The data in the WHDH is provided as primarily as reports with visualizations although there are additionally API endpoints to access the data directly.  The goal of this challenge was to use OpenAI to provide text and audio summarizations of PowerBI or other visualizations, for visually impaired or mobile data users.  A stretch goal was to allow the users to ask questions of the data in a more ad-hoc manner and have the analysis read back.  

<br />
<br />
<br />

## The Solution

Our team built two different solutions, one based on Python and the other on C#.  We focused on the “summarization engine” portion of the project and built solutions to record customer data requests, ingest data, summarize key points with GTP and read this back to the user.

<br />

![Architecture](https://github.com/microsoft/OpenAI-Hack-Group-5-Humanitarian/blob/main/Images/architecture%20screen%20shot.png)

<br />
<br />
<br />

## The Impact

At a very high level this is a tool to replace visualizations for PowerBI with text summaries enabling visually impaired and mobile users.  This extends further as users are also able to simply ask additional questions of the data.

As this code is easily called by serverless services such as Azure Functions or Logic Apps, our code is very extensible and easily embedded behind web apps or chat bots or by referencing voice captured through telephony solutions.  While our solutions would both require some modification by customers prior to implementation, this technological lift should be small.

The output however is a fully accessible replacement to PowerBI visualizations and "Ask a question of the data" functionality for both visually impaired as well as mobile or remote scenarios.

<br />
<br />
<br />

## How to Replicate the solution

This use case not unique to nonprofit or the WHO.  These ML models will ingest data and allow for text summarization and user Q&A functionality regardless of industry.  There are certain limitations due to data size, however our data scientists did provide recommendations and sample code for extensions.  This will be further discussed in the technical details below.

<br />
<br />
<br />

## Demos

<br />

![Python Demo](https://github.com/microsoft/OpenAI-Hack-Group-5-Humanitarian/blob/main/Demos/Python%20Demo%20Final.mp4)

<br />

![C# Demo](https://github.com/microsoft/OpenAI-Hack-Group-5-Humanitarian/blob/main/Demos/C%23%20Demo%20Final.mov)

<br />

## Cost Considerations

For both solutions, cost for our customers was a consideration.

The Python solution is currently using the following technology.

    Whisperlite Python Library - this is $0.006/minute
    Azure Function - to execute the Python code
    Azure Storage - to facilitate data movement
    Azure App Services - This could be used to host a front end web app.  However this is not a requirement.
    Azure OpenAI Services

The C# solution is using the following.

    Azure Cognitive Services - This is currently on free tier pricing.
    Azure Function or Logic Apps - To execute the C#
    Azure Storage - To facilitate data movement
    Azure App Services - This could be used to host a front end web app.  However this is not a requirement.
    Azure OpenAI Services
 
 Most of these services have a free tier, so development of this technology should be relatively cheap for customers.  Once this solution is in production, the cost of all of these services are based on the number of calls to the system.  Most of the calls to cognitive services are just a few cents per API call, so the cost of Azure would likely be derived more from the Azure infrastructure to support integration between this summarization engine and the front end appliation.
 
  
<br />
<br />
<br />

## Technical Details

Technical deals of each individual solution are contained in the readme files in the folders [Python](https://github.com/microsoft/OpenAI-Hack-Group-5-Humanitarian/tree/main/Python) and [C#](https://github.com/microsoft/OpenAI-Hack-Group-5-Humanitarian/tree/main/C%23).

<br />

### Technical Challenges

The biggest technical challange with this solution was in using OpenAI services for the generation of the data summary.  GPT is great at document summaries and great at language and conversation understanding, however most of this data is column data in the simplest form.  

In our initial testing, we were simiply asking for a summary or asking specific questions of the data, and specifying the WHO URL for the intended data set.  Surprisingly this generated excellent outputs.  Unfortunately when we examined the numerical output, the values did not corrospond to the current data in the visualizatoins.  Upon review of the models, it would appear that the answers were being genereated from GPT itself, and that either it had been trained on this WHO data or on data that contained similar infomration and that the data was simply old.  The result being that we could use GPT directly if we did not need 100% factual or more likely, up to date data.

Our goal then became to force the models to use the document provided and not the pretrained data in the model itself.  We attempted this in a few different ways.  We experimented with taking each row of columns and turning it into a sentence, and then passing that into the model as a parameter.  We also tried a couple different approaches of passing the values directly in as parameters.

We had success with each of these methods but with the result of limiting the overall data set sizes that can be utilized in this way.  Essentially you will run out of tokens to pass data and will be limited in the number of rows.  This limitation will be addressed in the future enhancements for this project.
<br />

### Future Enhancements

Our team did explore different solutions to this token and data limitation of GPT.  One solution would be allowing the model to be trained on the external data sets. Likely this would require additional data preparation such as creating sentences out of column data. 

The other option would be to pre-analyze the data.  In the future enhancements section of this repository, we have included a notebook that would take a numerical data set and extract "interesting" features.  These extracted features would then be useful to provide as parameters to the GPT calls and facilitate data set summarization to fulfill the requirements of this challange with larger data sets.  

The drawback to this method is that "interesting features" of the data may be different depending on the type of data being analyzed.  So additional data science work may be required to provide accurate preprocessing for summarization.
<br />
<br />
<br />


## Contributing

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.opensource.microsoft.com.

When you submit a pull request, a CLA bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

## Trademarks

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft 
trademarks or logos is subject to and must follow 
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship.
Any use of third-party trademarks or logos are subject to those third-party's policies.
