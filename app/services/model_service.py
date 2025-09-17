import joblib
import pandas as pd
from typing import List
from app.core.config import settings
from app.cache.redis_cache import set_cached_prediction,get_cached_prediction

model = joblib.load(settings.MODEL_PATH)

def predict_student_score(data:dict):
    cache_key = " ".join([str(val) for val in data.values()])
    cached = get_cached_prediction(cache_key)
    if cached:
        return cached
    input_data = pd.DataFrame([data])
    prediction = model.predict(input_data)[0]
    set_cached_prediction(cache_key, float(prediction))
    return float(prediction)

def predict_batch_student_scores(batch_data: List[dict]) -> List[float]:
    """
    Efficient batch prediction for multiple students.
    Optimized for memory usage and speed.
    """
    # Check cache for all entries first
    predictions = []
    uncached_indices = []
    uncached_data = []
    
    for i, data in enumerate(batch_data):
        cache_key = " ".join([str(val) for val in data.values()])
        cached = get_cached_prediction(cache_key)
        if cached:
            predictions.append(cached)
        else:
            predictions.append(None)  # Placeholder
            uncached_indices.append(i)
            uncached_data.append(data)
    
    # Batch predict uncached entries
    if uncached_data:
        # Create DataFrame once for all uncached predictions
        batch_df = pd.DataFrame(uncached_data)
        batch_predictions = model.predict(batch_df)
        
        # Cache and store results
        for idx, pred in zip(uncached_indices, batch_predictions):
            pred_float = float(pred)
            predictions[idx] = pred_float
            # Cache individual predictions
            cache_key = " ".join([str(val) for val in batch_data[idx].values()])
            set_cached_prediction(cache_key, pred_float)
    
    return predictions

