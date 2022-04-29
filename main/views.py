from django.views.generic import TemplateView
from django.shortcuts import render
from .models import Region
import numpy as np
np.random.seed(123)
import pandas as pd
from numpy.polynomial import polynomial as P


# Creating views
class EditorChartView(TemplateView):
    template_name = 'main/chart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        qs = Region.objects.all().values()
        data = pd.DataFrame(qs)

        values_air = dict()
        values_water = dict()
        years = [2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]

        for i in data["region_name"]:
            reg_data = data[data["region_name"] == i].sort_values(by='year', ascending=True)
            reg_data_val_air = list(reg_data['percent_air_pollution'])
            reg_data_val_air = [round(elem, 2) for elem in reg_data_val_air]

            x = reg_data_val_air[:-1]
            y = reg_data_val_air[1:]

            coefs_air_2, stats_air_2 = P.polyfit(x, y, 2, full=True)
            coefs_air_3, stats_air_3 = P.polyfit(x, y, 3, full=True)

            air_sum_squared_2 = stats_air_2[0]
            air_sum_squared_3 = stats_air_3[0]

            if air_sum_squared_2 <= air_sum_squared_3:

                val = reg_data_val_air[-1]
                y1 = coefs_air_2[0] + coefs_air_2[1] * val + coefs_air_2[2] * (val ** 2)
                reg_data_val_air.append(y1)
                val = reg_data_val_air[-1]
                y2 = coefs_air_2[0] + coefs_air_2[1] * val + coefs_air_2[2] * (val ** 2)
                reg_data_val_air.append(y2)

            elif air_sum_squared_3 < air_sum_squared_2:

                val = reg_data_val_air[-1]
                y1 = coefs_air_3[0] + coefs_air_3[1] * val + coefs_air_3[2] * (val ** 2) + coefs_air_3[3] * (val ** 3)
                reg_data_val_air.append(y1)
                val = reg_data_val_air[-1]
                y2 = coefs_air_3[0] + coefs_air_3[1] * val + coefs_air_3[2] * (val ** 2) + coefs_air_3[3] * (val ** 3)
                reg_data_val_air.append(y2)

            reg_data_val_air = [round(elem, 2) for elem in reg_data_val_air]

            temp_dict_air = {"vals": reg_data_val_air}

            values_air[i] = temp_dict_air

        regs_list = [*values_air]
        air_vals = []

        for keys, vals in values_air.items():
            for keys_2, vals_2 in vals.items():
                air_vals.append(vals_2)

        ###################################

        for i in data["region_name"]:
            reg_data = data[data["region_name"] == i].sort_values(by='year', ascending=True)
            reg_data_val_water = list(reg_data['percent_water_pollution'])
            reg_data_val_water = [round(elem, 2) for elem in reg_data_val_water]

            x = reg_data_val_water[:-1]
            y = reg_data_val_water[1:]

            coefs_water_2, stats_water_2 = P.polyfit(x, y, 2, full=True)
            coefs_water_3, stats_water_3 = P.polyfit(x, y, 3, full=True)

            water_sum_squared_2 = stats_water_2[0]
            water_sum_squared_3 = stats_water_3[0]

            if water_sum_squared_2 <= water_sum_squared_3:
                coefs_water = coefs_water_2
                a = coefs_water[0]
                b = coefs_water[1]
                c = coefs_water[2]

                val = reg_data_val_water[-1]
                y1 = a + b * val + c * (val ** 2)
                reg_data_val_water.append(y1)
                val = reg_data_val_water[-1]
                y2 = a + b * val + c * (val ** 2)
                reg_data_val_water.append(y2)
            else:
                coefs_water = coefs_water_3

                a = coefs_water[0]
                b = coefs_water[1]
                c = coefs_water[2]
                d = coefs_water[3]

                val = reg_data_val_water[-1]
                y1 = a + b * val + c * (val ** 2) + d * (val ** 3)
                reg_data_val_water.append(y1)
                val = reg_data_val_water[-1]
                y2 = a + b * val + c * (val ** 2) + d * (val ** 3)
                reg_data_val_water.append(y2)

            reg_data_val_water = [round(elem, 2) for elem in reg_data_val_water]

            temp_dict_water = {"vals": reg_data_val_water}

            values_water[i] = temp_dict_water

        water_vals = []

        for keys, vals in values_water.items():
            for keys_2, vals_2 in vals.items():
                water_vals.append(vals_2)

        context["regs_list"] = regs_list
        context["air_vals_list"] = air_vals
        context["water_vals_list"] = water_vals
        context["years"] = years

        return context


def home(request):
    return render(request, 'main/home.html', {})


def tables(request):
    return render(request, 'main/tables.html', {})