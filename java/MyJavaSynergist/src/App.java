public class App {
    public static void main(String[] args)
    {
        A_Inventory Inv1 = new BackPack(10, 10);
        A_Inventory Inv2 = new BackPack(10, 10);
        A_Inventory Inv3 = new BackPack(10, 10);
        
        while(Inv1.append(getMassFood()))
        {
            System.out.println("Append __mass food to 1");
        }
        while(Inv2.append(getMassFood()))
        {
            System.out.println("Append __mass food to 2");
        }
        while(Inv3.append(getMassFood()))
        {
            System.out.println("Append __mass food to 3");
        }


        while(Inv1.append(getSizeFood()))
        {
            System.out.println("Append size food to 1");
        }
        while(Inv2.append(getSizeFood()))
        {
            System.out.println("Append size food to 2");
        }
        while(Inv3.append(getSizeFood()))
        {
            System.out.println("Append size food to 3");
        }
    }
    public static A_Item getSizeFood()
    {
        return new Food(1, 7);
    }
    public static A_Item getMassFood()
    {
        return new Food(7, 1);
    }
}
