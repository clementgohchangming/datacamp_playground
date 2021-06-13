 # Use the .append() method to combine the tracks tables
metallica_tracks = tracks_ride.append(tracks_master, sort=False).append(tracks_st, sort=False)

# Merge metallica_tracks and invoice_items
tracks_invoices = metallica_tracks.merge(invoice_items, on='tid', how='inner')

print(tracks_invoices)

# For each tid and name sum the quantity sold
tracks_sold = tracks_invoices.groupby(['tid','name']).agg({'quantity': 'sum'})

print(tracks_sold)

# Sort in decending order by quantity and print the results
print(tracks_sold.sort_values('quantity', ascending=False))