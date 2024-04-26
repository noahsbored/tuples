def format_itins(itins): 
    result = ""
    for i, itinerary in enumerate(itins, start=1):
        traveler_name, origin, destination = itinerary
        result += f"Itinerary {i}: {traveler_name} - From {origin} to {destination}\n"
    return result


itins = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]
formatted_itins = format_itins(itins)
print(formatted_itins)

