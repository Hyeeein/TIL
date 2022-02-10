import folium

my_loc = folium.Map(location=[37.503550462750475, 127.0497652689724], zoom_start=18)
folium.Marker([37.503550462750475, 127.0497652689724], popup=folium.Popup('멀티캠퍼스 선릉', max_width=100)).add_to(my_loc)

my_loc.save('visual02.html')