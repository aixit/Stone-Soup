# -*- coding: utf-8 -*-
from .base import Updater

__all__ = ['Updater']
__all__.extend(subclass_.__name__ for subclass_ in Updater.subclasses)