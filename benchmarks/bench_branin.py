import numpy as np

from skopt.benchmarks import branin
from skopt import gp_minimize, forest_minimize, gbrt_minimize

bounds = [(-5.0, 10.0), (0.0, 15.0)]
n_calls = 200
optimizers = [("gp_minimize", gp_minimize),
              ("forest_minimize", forest_minimize),
              ("gbrt_minimize", gbrt_minimize)]

for name, optimizer in optimizers:
    print(name)
    results = []
    min_func_calls = []
    time_ = 0.0

    for random_state in range(10):
        print(random_state)
        if name == "gp_minimize":
            res = optimizer(
                branin, bounds, random_state=random_state, n_calls=n_calls,
                noise=1e-10)
        else:
            res = optimizer(
                branin, bounds, random_state=random_state, n_calls=n_calls)
        results.append(res)
        min_func_calls.append(np.argmin(res.func_vals) + 1)

    optimal_values = [result.fun for result in results]
    mean_optimum = np.mean(optimal_values)
    std = np.std(optimal_values)
    best = np.min(optimal_values)
    print("Mean optimum: " + str(mean_optimum))
    print("Std of optimal values" + str(std))
    print("Best optima:" + str(best))

    mean_fcalls = np.mean(min_func_calls)
    std_fcalls = np.std(min_func_calls)
    best_fcalls = np.min(min_func_calls)
    print("Mean func_calls to reach min: " + str(mean_fcalls))
    print("Std func_calls to reach min: " + str(std_fcalls))
    print("Fastest no of func_calls to reach min: " + str(best_fcalls))
