import os
import subprocess

from . import CompilerMeta


class LessCompiler(object, metaclass=CompilerMeta):
    supported_mimetypes = ['text/less', 'text/css']

    @classmethod
    def compile(cls, what, mimetype='text/less', include_path=None, debug=None):
        args = ['lessc']

        if not debug:
            args += ['--compress']

        if include_path:
            sep = ';' if os.name == 'nt' else ':'
            args += ['--include-path={}'.format(sep.join(include_path))]

        args += ['-']

        handler = subprocess.Popen(args, stdout=subprocess.PIPE,
                                   stdin=subprocess.PIPE,
                                   stderr=subprocess.PIPE, cwd=None)

        (stdout, stderr) = handler.communicate(input=what)
        if handler.returncode == 0:
            return stdout
        else:
            raise RuntimeError('Test this :S %s' % stderr)
