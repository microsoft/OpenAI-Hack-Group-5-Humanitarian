# WHO/WHDH Chart Data Text Summarization - Extracting Insights from Data for Visually Impaired

WHO's World Health Data Hub(WHDH) provides an interactive digital platform and trusted source for global health data, fulfilling WHO’s commitment to provide health data as a public good. The platform brings together an ambitious product stack to deliver an end-to-end solution for WHO data processes. From collection to use the platform provides a world class experience leveraging innovative technology to address challenges and pain points.

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

<br />
<br />
<br />

## How to Replicate the solution

This use case not unique to nonprofit or the WHO.  These ML models will ingest data and allow for text summarization and user Q&A functionality regardless of industry.  There are certain limitations due to data size, however our data scientists did provide recommendations and sample code for extensions.  


<br />
<br />
<br />

## Demos

<br />
<br />
<br />

## Cost Considerations

<br />
<br />
<br />

## Technical Details
<br />

### Technical Challenges

<br />

### Future Enhancements

<br />
<br />
<br />





As the maintainer of this project, please make a few updates:

- Improving this README.MD file to provide a great experience
- Updating SUPPORT.MD with content about this project's support experience
- Understanding the security reporting process in SECURITY.MD
- Remove this section from the README

> This repo has been populated by an initial template to help get you started. Please
> make sure to update the content to build a great experience for community-building.



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
