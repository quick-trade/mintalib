
"""
Mintalib Indicators

Indicators names are upper case.

Indicators offer a composable interface where a function is bound with its calculation parameters.
When instantiated with parameters an indicator yields a callable that can be applied to prices or series data.
Indicators support the `@` operator as syntactic sugar to apply the indicator to data.
So for example `SMA(50) @ prices` can be used to compute the 50 period simple moving average on `prices`,
insted of `SMA(50)(prices)`.

"""

# Do not edit! This file was generated by make-indicators.ipynb

from . import core
from .core import wrap_indicator
from .model import FuncIndicator

nan = float('nan')


__all__ = [
    'AVGPRICE', 'TYPPRICE', 'WCLPRICE', 'MIDPRICE', 'PRICE', 'CROSSOVER',
    'CROSSUNDER', 'FLAG', 'UPDOWN', 'SIGN', 'LOG', 'EXP', 'DIFF', 'LAG',
    'MIN', 'MAX', 'SUM', 'ROC', 'MAD', 'STDEV', 'SMA', 'EMA', 'RMA', 'WMA',
    'HMA', 'DEMA', 'TEMA', 'MA', 'RSI', 'ADX', 'PLUSDI', 'MINUSDI',
    'TRANGE', 'ATR', 'NATR', 'SAR', 'CCI', 'CMF', 'MFI', 'BOP', 'BBANDS',
    'KELTNER', 'KER', 'KAMA', 'MACD', 'PPO', 'SLOPE', 'RVALUE', 'FORECAST',
    'CURVE', 'STOCH', 'STREAK', 'EVAL'
]


@wrap_indicator(core.AVGPRICE)
def AVGPRICE():
    return FuncIndicator(core.AVGPRICE, params=locals())


@wrap_indicator(core.TYPPRICE)
def TYPPRICE():
    return FuncIndicator(core.TYPPRICE, params=locals())


@wrap_indicator(core.WCLPRICE)
def WCLPRICE():
    return FuncIndicator(core.WCLPRICE, params=locals())


@wrap_indicator(core.MIDPRICE)
def MIDPRICE():
    return FuncIndicator(core.MIDPRICE, params=locals())


@wrap_indicator(core.PRICE)
def PRICE(item: str = None):
    return FuncIndicator(core.PRICE, params=locals())


@wrap_indicator(core.CROSSOVER)
def CROSSOVER(level: float = 0.0, *, item: str = None):
    return FuncIndicator(core.CROSSOVER, params=locals())


@wrap_indicator(core.CROSSUNDER)
def CROSSUNDER(level: float = 0.0, *, item: str = None):
    return FuncIndicator(core.CROSSUNDER, params=locals())


@wrap_indicator(core.FLAG)
def FLAG(*, item: str = None):
    return FuncIndicator(core.FLAG, params=locals())


@wrap_indicator(core.UPDOWN)
def UPDOWN(up_level: float = 0.0, down_level: float = 0.0, *, item: str = None):
    return FuncIndicator(core.UPDOWN, params=locals())


@wrap_indicator(core.SIGN)
def SIGN(item: str = None):
    return FuncIndicator(core.SIGN, params=locals())


@wrap_indicator(core.LOG)
def LOG(*, item: str = None):
    return FuncIndicator(core.LOG, params=locals())


@wrap_indicator(core.EXP)
def EXP(*, item: str = None):
    return FuncIndicator(core.EXP, params=locals())


@wrap_indicator(core.DIFF)
def DIFF(period: int = 1, *, item: str = None):
    return FuncIndicator(core.DIFF, params=locals())


@wrap_indicator(core.LAG)
def LAG(period: int, *, item: str = None):
    return FuncIndicator(core.LAG, params=locals())


@wrap_indicator(core.MIN)
def MIN(period: int, *, item: str = None):
    return FuncIndicator(core.MIN, params=locals())


@wrap_indicator(core.MAX)
def MAX(period: int, *, item: str = None):
    return FuncIndicator(core.MAX, params=locals())


@wrap_indicator(core.SUM)
def SUM(period: int, *, item: str = None):
    return FuncIndicator(core.SUM, params=locals())


@wrap_indicator(core.ROC)
def ROC(period: int = 1, *, item: str = None):
    return FuncIndicator(core.ROC, params=locals())


@wrap_indicator(core.MAD)
def MAD(period: int = 20, *, item: str = None):
    return FuncIndicator(core.MAD, params=locals())


@wrap_indicator(core.STDEV)
def STDEV(period: int = 20, *, item: str = None):
    return FuncIndicator(core.STDEV, params=locals())


@wrap_indicator(core.SMA)
def SMA(period: int, *, item: str = None):
    return FuncIndicator(core.SMA, params=locals())


@wrap_indicator(core.EMA)
def EMA(period: int, *, adjust: bool = False, item: str = None):
    return FuncIndicator(core.EMA, params=locals())


@wrap_indicator(core.RMA)
def RMA(period: int, *, item: str = None):
    return FuncIndicator(core.RMA, params=locals())


@wrap_indicator(core.WMA)
def WMA(period: int, *, item: str = None):
    return FuncIndicator(core.WMA, params=locals())


@wrap_indicator(core.HMA)
def HMA(period: int, *, item: str = None):
    return FuncIndicator(core.HMA, params=locals())


@wrap_indicator(core.DEMA)
def DEMA(period: int, *, item: str = None):
    return FuncIndicator(core.DEMA, params=locals())


@wrap_indicator(core.TEMA)
def TEMA(period: int = 20, *, item: str = None):
    return FuncIndicator(core.TEMA, params=locals())


@wrap_indicator(core.MA)
def MA(period: int = 20, *, ma_type: str = None, item: str = None):
    return FuncIndicator(core.MA, params=locals())


@wrap_indicator(core.RSI)
def RSI(period: int = 14, *, item: str = None):
    return FuncIndicator(core.RSI, params=locals())


@wrap_indicator(core.ADX)
def ADX(period: int = 14):
    return FuncIndicator(core.ADX, params=locals())


@wrap_indicator(core.PLUSDI)
def PLUSDI(period: int = 14):
    return FuncIndicator(core.PLUSDI, params=locals())


@wrap_indicator(core.MINUSDI)
def MINUSDI(period: int = 14):
    return FuncIndicator(core.MINUSDI, params=locals())


@wrap_indicator(core.TRANGE)
def TRANGE(*, log_prices: bool = False, percent: bool = False):
    return FuncIndicator(core.TRANGE, params=locals())


@wrap_indicator(core.ATR)
def ATR(period: int = 14):
    return FuncIndicator(core.ATR, params=locals())


@wrap_indicator(core.NATR)
def NATR(period: int = 14):
    return FuncIndicator(core.NATR, params=locals())


@wrap_indicator(core.SAR)
def SAR(afs: float = 0.02, maxaf: float = 0.2):
    return FuncIndicator(core.SAR, params=locals())


@wrap_indicator(core.CCI)
def CCI(period: int = 20):
    return FuncIndicator(core.CCI, params=locals())


@wrap_indicator(core.CMF)
def CMF(period: int = 20):
    return FuncIndicator(core.CMF, params=locals())


@wrap_indicator(core.MFI)
def MFI(period: int = 14):
    return FuncIndicator(core.MFI, params=locals())


@wrap_indicator(core.BOP)
def BOP(period: int = 20):
    return FuncIndicator(core.BOP, params=locals())


@wrap_indicator(core.BBANDS)
def BBANDS(period: int = 20, nbdev: float = 2.0):
    return FuncIndicator(core.BBANDS, params=locals())


@wrap_indicator(core.KELTNER)
def KELTNER(period: int = 20, nbatr: float = 2.0):
    return FuncIndicator(core.KELTNER, params=locals())


@wrap_indicator(core.KER)
def KER(period: int = 10, *, item: str = None):
    return FuncIndicator(core.KER, params=locals())


@wrap_indicator(core.KAMA)
def KAMA(period: int = 10, fastn: int = 2, slown: int = 30, *, item: str = None):
    return FuncIndicator(core.KAMA, params=locals())


@wrap_indicator(core.MACD)
def MACD(n1: int = 12, n2: int = 26, n3: int = 9, *, item: str = None):
    return FuncIndicator(core.MACD, params=locals())


@wrap_indicator(core.PPO)
def PPO(n1: int = 12, n2: int = 26, n3: int = 9, *, item: str = None):
    return FuncIndicator(core.PPO, params=locals())


@wrap_indicator(core.SLOPE)
def SLOPE(period: int = 20, *, item: str = None):
    return FuncIndicator(core.SLOPE, params=locals())


@wrap_indicator(core.RVALUE)
def RVALUE(period: int = 20, *, item: str = None):
    return FuncIndicator(core.RVALUE, params=locals())


@wrap_indicator(core.FORECAST)
def FORECAST(period: int = 20, offset: int = 0, *, item: str = None):
    return FuncIndicator(core.FORECAST, params=locals())


@wrap_indicator(core.CURVE)
def CURVE(period: int = 20, *, item: str = None):
    return FuncIndicator(core.CURVE, params=locals())


@wrap_indicator(core.STOCH)
def STOCH(period: int = 14, fastn: int = 3, slown: int = 3):
    return FuncIndicator(core.STOCH, params=locals())


@wrap_indicator(core.STREAK)
def STREAK(*, item: str = None):
    return FuncIndicator(core.STREAK, params=locals())


@wrap_indicator(core.EVAL)
def EVAL(expr: str):
    return FuncIndicator(core.EVAL, params=locals())


