/*******************************************
 * answer 1: 427
 * answer 2: 558
 *
 * *****************************************/



#include <string>
#include <iostream>
#include <fstream>
#include <map>

void print_usage(const std::string app_name)
{
  std::cout << app_name << " <input_file>" << std::endl;
}

void compute_frequency(std::ifstream& input)
{
  std::multimap<long, long> frequencies;
  long frequency = 0;
  frequencies.insert( std::pair<long, long> (frequency,frequency) );

  while (!input.eof())
  {
    long freq_delta = 0;
    input >> freq_delta;

    if ( 0 == freq_delta ) 
    {
      if ( input.eof() )
      {
        input.clear();
        input.seekg(0, input.beg);
      }
      continue;
    }

    frequency += freq_delta;
    frequencies.insert( std::pair<long, long>(frequency, frequency) );
    
    if ( frequencies.count(frequency) > 1 )
    {
      std::cout << freq_delta << " => " << frequency << " (TWICE) ####################." << std::endl;
      break;
    }
    else
    {
      std::cout << freq_delta << " => " << frequency << std::endl;
    }    
  }

  std::cout << "There are " << frequencies.size() << " frequencies." << std::endl;
}

int main (int argc, char* argv[])
{
  if ( 1 < argc )
  {
    std::ifstream input;
    input.open(argv[1], std::ifstream::in);
    compute_frequency(input);
    input.close();
  }
  else
  {
    print_usage(argv[0]);
  }

  return (0);
}
