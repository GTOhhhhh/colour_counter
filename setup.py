from setuptools import setup, find_packages

setup(name='colour_counter',
      version='1.0',
      packages=find_packages(),
      install_requires=['flask',
                        'numpy',
                        'pytest',
                        'opencv-python',
                        'flask_socketio',
                        'numba',
                        'gevent'
                        ],
      )
