<?php
//They are not allow to use Python so I will use PHP
interface AdvancedArithmetic{
    public function divisorSum($n);
}

class Calculator implements AdvancedArithmetic{

    public function divisorSum($n)
    {
        $divisors = [];
        $i = 0;
        while ($i++ <= $n){
            if($n%$i==0){
                $divisors[] = $i;
            }
        }
        return array_sum($divisors);
    }
}

$n=intval(fgets(STDIN));
$myCalculator=new Calculator();
if($myCalculator instanceof AdvancedArithmetic)//checking if Calculator has implemented AdvancedArithemtic
{
    $sum=$myCalculator->divisorSum($n);
    echo "I implemented: AdvancedArithmetic\n".$sum;
}
else
{
    echo "Wrong answer";// You will get this output if you dont implement
}
?>