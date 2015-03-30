using AForge.Neuro;
using AForge.Neuro.Learning;
using CsvHelper;
using CsvHelper.Configuration;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Forecast
{
    class Program
    {
        static void Main(string[] args)
        {
            int windowSize = 10;

            ActivationNetwork network = new ActivationNetwork(new SigmoidFunction(), windowSize + 1, 4, 1);

            BackPropagationLearning teacher = new BackPropagationLearning(network);
            teacher.LearningRate = 0.1;
            teacher.Momentum = 0;

            List<TimePoint> points = null;
            using(StreamReader reader = new StreamReader("../data/series.csv"))
            {
                CsvConfiguration config = new CsvConfiguration();
                config.HasHeaderRecord = false;
                config.RegisterClassMap<TimePointMap>();

                var csv = new CsvReader(reader, config);
                points = csv.GetRecords<TimePoint>().ToList();
            }

            for (int i = 0; i < points.Count; i++)
            {
                var windows = points.Skip(i).Take(windowSize);

                double[] inputs = new double[windowSize];
                double[] output = new double[1];
                inputs[0] = points[windowSize].Time.TimeOfDay.TotalMinutes;
                output[0] = points[windowSize].Value;

                for (var j = 1; j < windows.Count(); j++)
                {
                    inputs[j] = windows.ElementAt(j).Value;
                }

                var error = teacher.Run(inputs, output);
                Console.WriteLine("Error = {0}", error);
            }
        }
    }
}
