import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# qualtities plotted
# squarre area is the town surface area (superf)
# color scale is the town population in 2011 (p11_pop)

# read data from csv file
# data from CAPP opendata http://opendata.agglo-pau.fr/index.php/fiche?idQ=27
df = pd.read_excel("Customer Success New.xlsx")
df = df.set_index("location_id")
df = df[["user_id", "company_id"]]
df2 = df.sort_values(by="user_id", ascending=False)

# treemap parameters
x = 0.
y = 0.
width = 100.
height = 100.
cmap = matplotlib.cm.viridis

# color scale on the population
# min and max values without Pau
mini, maxi = df2.company_id.min(), df2.company_id.max()
norm = matplotlib.colors.Normalize(vmin=mini, vmax=maxi)
colors = [cmap(norm(value)) for value in df2.company_id]
colors[1] = "#FBFCFE"

# labels for squares
#labels = ["hab" % (label) for label in zip(df2.index, df2.user_id), df2.company_id)]
#labels[11] = "MAZERES" % (df2["user_id"]["MAZERES-LEZONS"], df2["company_id"]["MAZERES-LEZONS"])

# make plot
fig = plt.figure(figsize=(12, 10))
fig.suptitle("Population et superficie des communes de la CAPP", fontsize=20)
ax = fig.add_subplot(111, aspect="equal")
ax = squarify.plot(df2.superf, color=colors, label=labels, ax=ax, alpha=.7)
ax.set_xticks([])
ax.set_yticks([])
ax.set_title("L'aire de chaque carré est proportionnelle à la superficie de la commune\n", fontsize=14)

# color bar
# create dummy invisible image with a color map
img = plt.imshow([df2.p11_pop], cmap=cmap)
img.set_visible(False)
fig.colorbar(img, orientation="vertical", shrink=.96)

fig.text(.76, .9, "Population", fontsize=14)
fig.text(.5, 0.1,
         "Superficie totale %d km2, Population de la CAPP : %d hab" % (df2.superf.sum(), df2.p11_pop.sum()),
         fontsize=14,
         ha="center")
fig.text(.5, 0.07,
         "Source : http://opendata.agglo-pau.fr/",
         fontsize=14,
         ha="center")

plt.show()