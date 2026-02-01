
 🌊 Disaster Evacuation Route Visualization (India)

📌 Project Overview

This project visualizes **disaster evacuation routes in India** on a map. It is designed to help understand and plan safe evacuation paths during natural disasters such as floods,earthquake and cyclone.

The current implementation displays an evacuation route from **Nagpur to Hyderabad** on an India map.



 🚨 Disaster Scenario

Disaster Type:Flood
Evacuation Route: Nagpur → Hyderabad
Purpose: Demonstrate how evacuation paths can be plotted and visualized geographically during emergencies.



🗺️ Map Visualization

* Base map: **India political map**
* Marked cities:

  * Nagpur (Source)
  * Hyderabad (Destination)
* Route is drawn using a line connecting the cities.

⚠️ Known Issue:
The plotted evacuation route does not perfectly align with the actual geographical positions of the cities on the map. Some intermediate labels (e.g., Jaipur, Bhopal) appear visually closer to the route even though they are not part of the real path.

This happens due to:

* Approximate pixel-based coordinates
* Static image mapping instead of latitude–longitude plotting



🛠️ Technologies Used

* **Python**
* **Matplotlib**
* **PIL (Python Imaging Library)**
* Static India map image





 ⚙️ How It Works

1. A base image of India is loaded.
2. City positions are defined using **approximate coordinates**.
3. A line is drawn from the source city (Nagpur) to the destination (Hyderabad).
4. The final image displays the evacuation route along with city markers and labels.


🚀 Future Improvements

* Use **latitude–longitude coordinates** with libraries like **Folium or GeoPandas**
* Integrate **real disaster data APIs**
* Add **multiple evacuation routes**
* Interactive zoomable map
* Real distance calculation (in km)



 📖 Conclusion

This project serves as a **conceptual and visual demonstration** of disaster evacuation routing in India. While the current map alignment is approximate, it lays the groundwork for more accurate and scalable evacuation planning systems.




Just tell me 😊
