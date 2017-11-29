import datetime as dt
from dateutil.relativedelta import relativedelta
from calendar import monthrange
from scipy import optimize


class Datetime:

    @staticmethod
    def eomonth(date, i):
        date = date + relativedelta(months=i)
        return dt.date(date.year, date.month, monthrange(date.year, date.month)[1])


class Finance:
    @staticmethod
    def xnpv(rate, cashflows):
        """
        Calculate the net present value of a series of cashflows at irregular intervals.

        Args:
            rate: the discount rate to be applied to the cash flows

            cashflows: a list object in which each element is a tuple of the form (date, amount), where date is a
            python datetime.date object and amount is an integer or floating point number. Cash outflows (
            investments) are represented with negative amounts, and cash inflows (returns) are positive amounts.

        Returns:
            Returns a single value which is the NPV of the given cash flows.

        Note: The Net Present Value is the sum of each of cash flows discounted back to the date of the first cash
        flow. The discounted value of a given cash flow is A/(1+r)**(t-t0), where A is the amount, r is the discout
        rate, and (t-t0) is the time in years from the date of the first cash flow in the series (t0) to the date of
        the cash flow being added to the sum (t).
        """

        chron_order = sorted(cashflows, key=lambda x: x[0])
        t0 = chron_order[0][0]  # t0 is the date of the first cash flow

        return sum([cf / (1 + rate) ** ((t - t0).days / 365.0) for (t, cf) in chron_order])

    @staticmethod
    def xirr(cashflows, guess=0.1):
        """
        Calculate the Internal Rate of Return of a series of cashflows at irregular intervals.

        Args:
            cashflows: a list object in which each element is a tuple of the form (date, amount), where date is a
            python datetime.date object and amount is an integer or floating point number. Cash outflows (
            investments) are represented with negative amounts, and cash inflows (returns) are positive amounts.

            guess (optional, default = 0.1): a guess at the solution to be used as a starting point for the numerical
            solution.

        Returns:
            Returns the IRR as a single value

        Note: The Internal Rate of Return (IRR) is the discount rate at which the Net Present Value (NPV) of a series
        of cash flows is equal to zero. The NPV of the series of cash flows is determined using the xnpv function in
        this module. The discount rate at which NPV equals zero is found using the secant method of numerical solution.

        """
        return optimize.newton(lambda r: Finance.xnpv(r, cashflows), guess)
