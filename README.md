# sprint4-project
This is my project for TripleTen Sprint 4: Software Development Tools 

The purpose of this project is to demonstrate that I can write and deploy a simple web app.

The app displays vehicle data, plots several charts, and features an interactive element.

Plots:
- Bar chart of manufacturer by condition
- Bar chart of vehicle type by paint color
- Histogram of odometer by type (with a checkbox for outlyers > 300,000 miles)
- Scatterplot of price by model year (with a checkbox for model years since 1960)
- Histograms for designs of user selected manufacturer and type (with a checkbox to normalize)

Libraries used:
- pandas
- plotly.express
- streamlit

Dataset:
- vehicles_us.csv (https://practicum-content.s3.us-west-1.amazonaws.com/datasets/vehicles_us.csv)

How to Run Locally:
- Clone the repository: git clone https://github.com/uberbeek/sprint4-project
- Install the required Python packages: pip install -r requirements.txt
- Run the Streamlit app: streamlit run app.py
- The app should now be available at http://localhost:8501