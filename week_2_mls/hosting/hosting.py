from huggingface_hub import HfApi
import os
from week2_mls.config import HF_REPO_ID

api = HfApi(token=os.getenv("HF_TOKEN"))
api.upload_folder(
    folder_path="week_2_mls/deployment",     # the local folder containing your files
    repo_id=HF_REPO_ID,          # the target repo
    repo_type="space",                      # dataset, model, or space
    path_in_repo="",                          # optional: subfolder path inside the repo
)
