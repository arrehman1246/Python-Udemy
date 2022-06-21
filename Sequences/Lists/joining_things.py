flowers = [
    "Daffodil",
    "Evening Primrose",
    "Hydrangea",
    "Iris",
    "Lavender",      # join is a str method, so we can't add int in list
    "Sunflower",
    "Tiger Lily",
]

# for flower in flowers:
#     print(flower)

separator = ", "
output = separator.join(flowers)
print(output)

print(",".join(flowers))
