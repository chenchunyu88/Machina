
#include <boost/python/def.hpp>
#include <boost/python/list.hpp>
#include <boost/python/module.hpp>

using namespace std;
namespace bp = boost::python;


bp::list compute_cost(float plan_cost, float ded, float co_ins, float oop,
                      float com_contri, float self_contri, float tax_fac,
                      int iter=300)
{
    float raw, tmp1, tmp2, cost_i;
    bp::list cost;

    for (int i = 1; i <= iter; i++)
    {
        raw = i * 100;
        tmp1 = self_contri*tax_fac;
        tmp2 = ded + co_ins*(raw - ded);

        if (self_contri <= ded)
        {
            if (raw <= self_contri) {
                cost_i = raw*tax_fac;
            } else if (raw <= ded) {
                cost_i = tmp1 + raw - self_contri;
            } else {
                cost_i = tmp1 + min<float>(oop, tmp2) - self_contri;
            }
        }
        else
        {
            if (raw <= ded) {
                cost_i = raw*tax_fac;
            } else if (tmp2 <= self_contri) {
                cost_i = tmp2*tax_fac;
            } else {
                cost_i = tmp1 + min<float>(oop, tmp2) - self_contri;
            }
        }

        cost.append(plan_cost*tax_fac + cost_i - com_contri);
    }
    return cost;
}


BOOST_PYTHON_MODULE(core)
{
    using namespace boost::python;
    def("compute_cost", compute_cost);
}

