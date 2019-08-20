from setuptools import setup, find_packages

setup(name='colour_counter',
      version='1.0',
      packages=find_packages(),
      install_requires=['Flask',
                        'numpy',
                        'pytest',
                        'opencv-python',
                        'Flask_socketio',
                        'numba',
                        'gevent'
                        ],
      )
