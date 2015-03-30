using CsvHelper.Configuration;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Forecast
{
    public class TimePointMap
        : CsvClassMap<TimePoint>
    {
        public TimePointMap()
        {
            Map(m => m.Time).Index(0);
            Map(m => m.Value).Index(1);
        }
    }

    public class TimePoint
    {
        public DateTime Time { get; set; }

        public double Value { get; set; }
    }
}
