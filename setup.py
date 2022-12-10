from setuptools import setup, find_packages

setup(
  name = 'PaLM-rlhf-pytorch',
  packages = find_packages(exclude=[]),
  version = '0.0.1',
  license='MIT',
  description = 'PaLM + Reinforcement Learning with Human Feedback - Pytorch',
  author = 'Tinc0 Chan',
  author_email = 'tincochan@foxmail.com',
  long_description_content_type = 'text/markdown',
  url = 'https://github.com/tincochan/PaLM-rlhf-pytorch',
  keywords = [
    'artificial intelligence',
    'deep learning',
    'transformers',
    'attention mechanism',
    'reinforcement learning',
    'human feedback'
  ],
  install_requires=[
    'einops>=0.6',
    'numpy',
    'torch>=1.6',
    'tqdm'
  ],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
  ],
)
