import Abstract.*;
import Inventory_System.*;
import Items.Food;

public class App {
    public static void main(String[] args)
    {
        A_Inventory Inv1 = new Inventory_Backpack(10, 10, 4);
        A_Inventory Inv2 = new Inventory_Backpack(10, 10, 3);
        A_Inventory Inv3 = new Inventory_Backpack(10, 10, 2);
        
        A_Folder Folder1 = new Folder_Chest(1);

        System.out.println(Folder1.append(Inv1));
        System.out.println(Folder1.append(Inv2));
        System.out.println(Folder1.append(Inv3));

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
