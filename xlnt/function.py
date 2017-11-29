import datetime as dt
from dateutil.relativedelta import relativedelta
from calendar import monthrange
from scipy import optimize
import numpy as np


class Datetime:

    @staticmethod
    def edate(start_date, months):
        """
        Args:
            start_date: A datetime object that represents the starting date.
            months: The number of months before or after start_date.

        Returns:
            Returns the datetime that represents the date that is the indicated number of months before or
            after a specified date (the start_date). Use edate to calculate maturity dates or due dates that fall on the
            same day of the month as the date of issue.

        """
        return start_date + relativedelta(months=months)

    @staticmethod
    def eomonth(start_date, months):
        """
        Args:
            start_date: A datetime object that represents the starting date.
            months: The number of months before or after start_date.

        Returns:
            Returns the datetime of the last day of the month before or after a specified number of months.

        """
        date = start_date + relativedelta(months=months)
        return dt.date(date.year, date.month, monthrange(date.year, date.month)[1])

    @staticmethod
    def now():
        """
        Returns:
            Returns the current date and time.

        """
        return dt.datetime.now()

    @staticmethod
    def today():
        """
        Returns:
            Returns today's date.
        """

        return dt.date.today()


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


class Math:

    @staticmethod
    def sumproduct(lists):
        """
        Multiplies corresponding components in the given arrays, and returns the sum of those products.

        Args:
            lists: List of lists whose components you want to multiply and then add.

        Returns:

        TODO:
            Add optional criteria.

        """

        product_arr = [1]

        for list_ in lists:
            product_arr *= np.array(list_)

        return np.sum(product_arr)
