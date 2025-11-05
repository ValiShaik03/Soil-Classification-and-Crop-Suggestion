import pickle

def load_model(model_path, scaler_path):
    try:
        model = pickle.load(open(model_path, 'rb'))
        scaler = pickle.load(open(scaler_path, 'rb'))
        return model, scaler
    except:
        return None, None
