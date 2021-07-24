# Scaling fish data for clustering
You are given an array samples giving measurements of fish. Each row represents an individual fish. The measurements, such as weight in grams, length in centimeters, and the percentage ratio of height to length, have very different scales. In order to cluster this data effectively, you'll need to standardize these features first. In this exercise, you'll build a pipeline to standardize and cluster the data.

These fish measurement data were sourced from the Journal of Statistics Education.

# Instructions
- yImport:
- ymake_pipeline from sklearn.pipeline.
- yStandardScaler from sklearn.preprocessing.
- yKMeans from sklearn.cluster.
- yCreate an instance of StandardScaler called scaler.
- yCreate an instance of KMeans with 4 clusters called kmeans.
- yCreate a pipeline called pipeline that chains scaler and kmeans. To do this, you just need to pass them in as arguments to make_pipeline().
