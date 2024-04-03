from .eval import RunnerBasicEval
from .train import RunnerBasicTrain
from .sparsity import RunnerPrunedSparsity

SW_RUNNERS = {
    "basic_evaluation": RunnerBasicEval,
    "basic_train": RunnerBasicTrain,
    "basic_sparsity": RunnerPrunedSparsity,
}


def get_sw_runner(name: str, model_info, task: str, dataset_info, accelerator, config):
    if name not in SW_RUNNERS:
        raise ValueError(f"Software runner {name} is not supported.")

    return SW_RUNNERS[name](model_info, task, dataset_info, accelerator, config)
