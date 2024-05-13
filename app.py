from flask import Flask, render_template
import folium

app = Flask(__name__)


@app.route('/')
def home():
    # Create Folium map
    m = folium.Map(location=[22.5454, 88.3333], zoom_start=10)  # Default location

    # Add heart-shaped icons for visited places
    places = {
        "Prothom Alap: Maths Tuition": (22.471966834748994, 88.34031880974234),
        "Bondhubhab: Physics Tuition": (22.476846060796543, 88.34824638605211),
        "Dhansiri": (22.481790164441577, 88.34596378403674),
        "Dekhe lekha: Chemistry Tuition": (22.472652317988185, 88.33966927296895),
        "Bari": (22.5726, 88.3676),
        "Waiting @Netaji Metro": (22.481142122719667, 88.3459860091707),
        "Adda at Mohorkunjo": (22.543916023634903, 88.3450263803368),
        "Cinema at Nandan": (22.54254314530729, 88.34559681333485),
        "Bottle Cricket @Elliot Park": (22.54815729263626, 88.34810759382941),
        "Motion Sickness Incident": (22.57636881304261, 88.42705075335292),
        "Na Ru Meg Date": (22.514049658374976, 88.34920396684342),
        "Lake Mall Adda & Shopping": (22.5165752318844, 88.34905223800769),
        "Tajpur": (21.649752896035956, 87.61287400914549),
        "Rashbeharir oligoli": (22.516057151896348, 88.3475521969944),
        "School er Saraswati Pujo": (22.477537917202056, 88.34691749567808),
        "kaather bench @Garia Railstation": (22.47283477576418, 88.39813381102144),
        "A Pronto without burger": (22.51680579861661, 88.36459442636617),
        "Badminton@Wireless Park": (22.482095988734162, 88.34739142636506),
        "Olypub": (22.55370221799586, 88.35218087100894),
        "Kathi korte korte Kaathi roll": (22.55379207873769, 88.35220769568049),
        "Valobasha ar Boimela": (22.587011359447377, 88.42146277138853),
        "Shongram@TCS Gitobitan": (22.578431831044867, 88.43019019799901),
        "Boiparay anagona": (22.57379797854428, 88.36202031024547),
        "Ice Cream @Tollygunge Metro": (22.496258097724272, 88.34465035149088),
        "Maddox Square- A must": (22.526706453656686, 88.35487751102305),
        "Esplanade e kenakata": (22.56036679447137, 88.35262968818921),
        "Gariahat e chorom hata": (22.519086147577912, 88.36446518591372)
    }

    for place, coordinates in places.items():
        folium.Marker(
            location=coordinates,
            popup=place,
            icon=folium.Icon(color='pink', icon='heart')
        ).add_to(m)

    # Convert the map to HTML
    map_html = m._repr_html_()

    return render_template('index.html', map_html=map_html)


if __name__ == '__main__':
    app.run(debug=True)
