from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig:      ## It shows what are inputs to DataIngestion Module.
    root_dir: Path
    source_URL: Path
    local_data_file: Path
    unzip_dir: Path

@dataclass
class DataTransformationConfig:
    root_dir: Path
    data_path: Path
    tokenizer_name: Path

@dataclass
class ModelTrainerConfig:    
    ## These all variables will be required as an output of Model Trainer
    
    # 1st Three (3) variables from config.yaml
    root_dir: Path
    data_path: Path
    model_ckpt: Path

    # All Remaining (9) from params.yaml
    num_train_epochs: int
    warmup_steps: int
    per_device_train_batch_size: int
    weight_decay: float
    logging_steps: int
    evaluation_strategy: str
    eval_steps: int
    save_steps: float
    gradient_accumulation_steps: int

