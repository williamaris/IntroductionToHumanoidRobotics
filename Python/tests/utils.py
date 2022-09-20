import os
import json
import numpy as np

class MatlabEnv:
    def __init__(self, dir, results_db="mresults.json"):
        
        self.results_db_file = os.path.join(os.path.dirname(__file__), results_db)

        if not os.path.exists(self.results_db_file):
            with open(self.results_db_file, "w") as f:
                json.dump({}, f, indent=4)

        with open(self.results_db_file, "r") as f:
            self.results_db = json.load(f)

        self.files = {}

        self.dir = dir
        for root, dirs, files in os.walk(dir):
            for name in files:
                self.files[name] = root


    def run_func(self, func, force_exec = False):

        if self.results_db.get(func) is not None and not force_exec:
            if type(self.results_db[func]) == list:
                return np.array(self.results_db[func])
            
            return self.results_db[func]

        res = self.__run_func(func)

        if type(res).__module__ == 'numpy':
            self.results_db[func] = res.tolist()

        with open(self.results_db_file, "w") as f:
            json.dump(self.results_db, f, indent=4)

        return res


    def clear_db(self):
        with open(self.results_db_file, "w") as f:
            json.dump({}, f, indent=4)

        self.results_db = {}


    def __run_func(self, func, raw_output=False):
        cmd = 'matlab -batch "cd('
        
        matlab_dir = self.files.get(func.strip().split('(')[0] + '.m')

        if matlab_dir is None:
            return

        cmd += "'" + matlab_dir + "'); "
        cmd += 'res = ' + func + ';'
        cmd += 'disp(res);'
        cmd += 'whos res;'
        cmd += 'quit;"'

        n_of_lines_license = 4
        out = os.popen(cmd).read().split('\n')[n_of_lines_license:-2]

        if raw_output:
            return '\n'.join(out)

        out_last_line = out[-1].split()
        
        whos = {
            "size": [int(item) for item in out_last_line[1].split('x')],
            "bytes": int(out_last_line[2]),
            "class": out_last_line[3].strip()
        }

        raw_data = out[:-4]

        if whos["class"] == 'char':
            return "\n".join(raw_data)

        if whos["class"] == 'double':
            data =  [float(item) for item in " ".join(raw_data).split()]
            mat = np.array(data)
            mat = np.reshape(mat, whos["size"])
            
            return mat

        return "\n".join(raw_data)


if __name__ == '__main__':
    matlab_env = MatlabEnv(dir="../../Matlab")
    res = matlab_env.run_func("Rroll(0.7)")
    print(res)