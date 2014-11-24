var map = L.map('map').setView([40.7241745, -73.9841674], 13);

L.tileLayer('http://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile/{z}/{y}/{x}', {
	attribution: 'Tiles &copy; Esri &mdash; Source: Esri, DeLorme, NAVTEQ, USGS, Intermap, iPC, NRCAN, Esri Japan, METI, Esri China (Hong Kong), Esri (Thailand), TomTom, 2012'
}).addTo(map);


$("button").click(function () {
    if($(this).attr("id") == "Day") {
        geojsonLayer = L.geoJson(pathData, {
    style: function(feature) {
        return {color: feature.properties.DayColor};
    },
    pointToLayer: function(feature, latlng) {
        return new L.CircleMarker(latlng, 
            {stroke: false, radius: 6.5, fillOpacity: 0.85});
    },
    onEachFeature: function (feature, layer) {
        layer.bindPopup(feature.properties.TimeOfDay);
    }
                                    });
        map.addLayer(geojsonLayer);
        
    } else if ($(this).attr("id") == "Week"){
        geojsonLayer = L.geoJson(pathData, {
    style: function(feature) {
        return {color: feature.properties.WeekDayTypeColor};
    },
    pointToLayer: function(feature, latlng) {
        return new L.CircleMarker(latlng, 
            {stroke: false, radius: 6.5, fillOpacity: 0.55});
    },
    onEachFeature: function (feature, layer) {
        layer.bindPopup(feature.properties.WeekDayType);
    }
                                    });
        map.addLayer(geojsonLayer);
    } else {
        geojsonLayer = L.geoJson(pathData, {
    style: function(feature) {
        return {color: feature.properties.WeekColor};
    },
    pointToLayer: function(feature, latlng) {
        return new L.CircleMarker(latlng, 
            {stroke: false, radius: 6.5, fillOpacity: 0.85});
    },
    onEachFeature: function (feature, layer) {
        layer.bindPopup(feature.properties.Week);
    }
                                    });
        map.addLayer(geojsonLayer);
    }

});

