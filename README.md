# Introduction to NSE-FNO-expiry-calculator

This package gives you an easy methods to calculate near and far weekly and monthly expiry dates which also considers NSE holiday calendar.

## Installation

    pip install nse_fno_expiry_calculator
    // if you are using pipenv, then execute below
    pipenv install nse_fno_expiry_calculator

## Usage

There are 4 methods which reurns near and far weekly and monthly expiry dates

    # print('today is '+str(pendulum.now().date()))
    # print('nearest weekly exp is '+str(getNearestWeeklyExpiryDate()))
    # print('next weekly exp is '+str(getNextWeeklyExpiryDate()))
    # print('nearest monthly exp is '+str(getNearestMonthlyExpiryDate()))
    # print('next month exp is '+str(getNextMonthlyExpiryDate()))
