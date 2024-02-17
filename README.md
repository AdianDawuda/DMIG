# Domestic Migration in Germany

![DMIG logo](display_images/dmig.png)

This project provides a Spatial Data Infrastructure (SDI) that allows for the analyses and visualization of annual domestic migration flows within Germany. We utilize statistical migration data from the GENESIS-Online platform and federal-state boundary data from Eurostat to map these movements. The acquisition, integration, and storage of migration statistics and spatial information is conducted programmatically using the Python programming language and a PostGIS spatial database. This approach reduces manual effort and increases the overall repeatability and efficiency of the workflow. Our data is published using a Web Feature Service (WFS) created by GeoServer. An example dashboard visualization is created using ArcGIS Insights. This dashboard aims to provide an interactive platform for our stakeholders to explore an excerpt of the data and may serve as inspiration for further custom applications.

## Wiki

The project's wiki can be found [here](https://git.sbg.ac.at/s1093093/dmig/-/wikis/DMIG-Wiki). It provides more in-depth information about the project, its status, and how to replicate the results.

## Authors

Adian Dawuda | adian.dawuda@stud.plus.ac.at

Felix Schachtschneider | felix.schachtschneider@stud.plus.ac.at

## License

See the [LICENSE](https://git.sbg.ac.at/s1093093/dmig/-/blob/main/LICENSE) file for license rights and limitations ([GPL v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html)).
