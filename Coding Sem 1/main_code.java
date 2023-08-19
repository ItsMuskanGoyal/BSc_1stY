import java.util.*;

//import javax.lang.model.util.ElementScanner14;
public class main_code{
    // @param args
    public static void main(String args[]) {

        System.out.println(" Muskan goyal");

        
        
        //To take some input sc is just word use diffrent word everytime
        System.out.println("Write a line to get a copy");
        Scanner ab= new Scanner(System.in);
        String Name= ab.nextLine();
        System.out.println(Name);

        //to take value in numbers nextInt
        System.out.println("Any Number");
        int K= ab.nextInt();
        System.out.println(K);


        //Scanner kb = new Scanner(System.in);
        // I tried to see that above line written once is
        //capable taking input  multiple times
        System.out.println("Write 2 int to get Sum");
        int a= ab.nextInt();
        int b= ab.nextInt();
        int sum= a+b;
        System.out.println(sum);

        //Finding product
        System.out.println("Write 2 int for multiplication");
        int m= ab.nextInt();
        int n= ab.nextInt();
        int product= m*n;
        System.out.println(product);

        //Finding Area of circle 
        System.out.println("Enter value of r for area");
        int r= ab.nextInt();
        float Area = 22*r*r/7;
        System.out.println(Area);

        //Finding Area of circle
        System.out.println("Enter value of r for area");
        float rad= ab.nextFloat();
        float ar = 3.14f *rad *rad;
        System.out.println(ar);
        
        

        Scanner sc = new Scanner (System.in);


        
        System.out.println("Type casting of float into int");
        float a67 = sc.nextFloat();
        int b88= (int)a67;
        System.out.println(b88); 

        
        //Type promotion due to operation like +-
        //smaller to bigger data type
        float f1 = 29.38f;
        int int01 = 323;
        byte byte01= 2;
        float ans01= f1+int01-byte01;
        System.out.println(ans01);

        //Question 3 item total bill + 18% gst
        System.out.println("Enter 3 number");
        float item1= sc.nextFloat();
        float item2= sc.nextFloat();
        float item3= sc.nextFloat();
        float bill= item1+ item2+ item3;
        float totalbill = bill + bill* 0.18f;
        System.out.println(totalbill);


        // If else statements
        int int03=10;
        int int02=6;
        if(int02>int03){
        System.out.println("A>B");}
        else{
        System.out.println("B>A");
        } 
        

        //Checking odd or even
        System.out.println("Enter a number for even and odd check");
        int num01 = sc.nextInt();
        if(num01%2==0)
        System.out.println("Num is even");
        else if (num01%3==0)
        System.out.println("Num div by 3");
        else
        System.out.println("Num is odd");
        


        //Tax calculation
        float tax=0;
        System.out.println("Enter your income");
        float income05 = sc.nextFloat();
        if(income05<=200000)
            tax=0;
        else if (income05>200000 && income05<=500000)
            tax= (float) (income05 *0.2);
        else
           tax= (float) (income05 *0.5);
        System.out.println("Tax is"+ tax);

        
        // Ternanry operator
        // variable= condition? statement: statement;

    
        int number04 = 104263;
        String type02 = ((number04%2)==0)? "even": "odd";
        System.out.println(type02);

        //check a student is pass or fail

        System.out.println("Enter your marks to check pass or fail");
        float marks = sc.nextFloat();
        String grade03=marks>33? "Pass": "Fail";
        System.out.println("You "+ grade03+ " in examination");
        



        //Switch statement
        char ch3= '+';
        switch (ch3){
            case '+' : System.out.println("Icecream");
            break;
            default : System.out.println("Oreo shake");
        }

        //calculator
        System.out.println("Enter numbers");
        float value3 = sc.nextFloat();
        float value4 = sc.nextFloat();
        char operator88= sc.next().charAt(0);

        switch(operator88){
            case '+' : System.out.println(value3+value4); break;
            case '-' : System.out.println(value3-value4); break;
            case '*' : System.out.println(value3*value4); break;
            case '/' : System.out.println(value3/value4); break;
            default :  System.out.println("Wrong operator");
        }

        // While loop
        int loopcounter =0 ;
        while(loopcounter<10){
            System.out.println("hi");
            loopcounter=  loopcounter+1;
            loopcounter++;
        }
        
        //Sum of n numbers
        System.out.println("Enter n to find sum upto n numbers like factorial");
        float value12 = sc.nextFloat();
        float sum77 = 0;
        float i2=1;
        while(i2<=value12){
            sum77 = sum77 + i2;
            i2++;
        }
        System.out.println(sum77);
        

        
        //For loop Syntax
        System.out.println("Enter for FOR loop");

        for(int i = 1; i<=5; i++)
        {
            System.out.println("I will definately complete it soon");
        }

        //While loop to reverse print a number
        System.out.println("Enter number to reverse it");
        int n4= sc.nextInt();
        while(n4>0){
            int lastdigit44= n4%10;
            System.out.print(lastdigit44);
            n4/=10;}


        //Do while loop
        int counter56= 1;
        do{
            System.out.println("Hello World");
            counter56 ++;
        } while (counter56 < 5);

        // Break and continue statement
        for(int i45=0; i45<5; i45++)
        {
            if (i45==3){
                break;
            }
            System.out.println("value of I"+ i45);
        }
        
        // Break statement = It close the loop
        System.out.println("Enter number which is multiple of 10");
        do{
        int number87= sc.nextInt();
        if(number87%10==0){
            break;
        }
        System.out.println(number87);
        }while(true);
        




    }
}


