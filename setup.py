from distutils.core import setup

setup(name='colour_counter',
      version='1.0',
      py_modules=['app', 'services.count_areas', 'utils.disjoint_set', 'utils.img_bin_converter', 'utils.union_find'],
      packages=['flask',
                'numpy',
                'pytest',
                'opencv-python',
                'flask_socketio',
                # 'numba',
                ],
      )
