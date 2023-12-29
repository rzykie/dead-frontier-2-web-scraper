import httpx
import json
from selectolax.parser import HTMLParser
import re

url = "https://deadfrontier2.fandom.com/wiki/Unique_Pistol"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}


response = httpx.get(
    url,
    headers=headers,
)

# response.text is the HTMl
html = HTMLParser(response.text)

rows = html.css("table.customtable tbody tr")
# for row in rows:
#     # Extract pistol name if available
#     pistol_name_element = row.css("th span b")
#     pistol_name = pistol_name_element[0].text() if pistol_name_element else "N/A"

#     if pistol_name != "N/A":
#         # Add the pistol name to the dictionary with a placeholder value
#         pistol_dict[pistol_name] = "Description or any other relevant info"
# use keyword
# pistol_list = [
#     {"id": unique_id, "name": row.css("th span b")[0].text(), "percentage": 10}
#     for unique_id, row in enumerate(rows, start=1)
#     if row.css("th span b")
# ]
div = html.css("table.customtable tbody tr:nth-child(2) td div")
# spans_with_br = div.css("span br")
result_list = []
pattern = re.compile(r"(?P<key>[^:]+):\s*(?P<value>[^:]+)")

for di in div:
    matches = pattern.findall(di.text())
    result_dict = {key.strip(): value.strip() for key, value in matches}
    result_list.append(result_dict)
breakpoint()
key_phrases = [
    "Base Item",
    "Equipment Slot",
    "Level Required",
    "Weapon Type",
    "Body Damage Per Hit",
    "Attacks Per Sec",
    "Stun Duration",
    "Knockback Distance",
    "Noise Radius",
    "Headshot Damage",
    "Ammo Type",
    "Accuracy Error",
    "Aim Time",
    "Range",
    "Reload Time",
    "Clip Size",
    "Effective DPS",
    "Scrap Value",
]


# Define a regex pattern to capture key and value pairs
pattern = re.compile(r"(?P<key>[^:]+):(?P<value>[^:]+)")

for sec in second_tr:
    result_dict = {}
    # Iterate over key phrases and split the text
    for key_phrase in key_phrases:
        match = pattern.search(sec.text())
        if match:
            result_dict[key_phrase] = match.group("value").strip()

    # Append the dictionary to the list
    result_list.append(result_dict)
breakpoint()
# Check if the second tr exists
if second_tr:
    # Get the parent span element after the second tr
    parent_span = second_tr[0].parent("span")

    # Check if the parent span exists
    if parent_span:
        # Print the text content of the parent span
        print(parent_span.text(strip=True))
    else:
        print("Parent span not found after the second tr.")
else:
    print("Second tr not found in the specified table.")

breakpoint()
with open("pistol_names.json", "w") as json_file:
    json.dump(pistol_list, json_file, indent=2)

# Print a message indicating the successful operation
print("Pistol names have been saved to pistol_names.json")
