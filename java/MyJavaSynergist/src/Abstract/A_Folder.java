package Abstract;
import java.util.ArrayList;

public abstract class A_Folder {

    private double max_convenience;
    private double current_convenience;
    private ArrayList<A_Inventory> folded_inventories;
    
    public A_Folder (double max_convenience)
    {
        this.max_convenience = max_convenience;
        this.current_convenience = 0;
        this.folded_inventories = new ArrayList<>();
    }

    public boolean append(A_Inventory inventory)
    {
        if (this.current_convenience + inventory.getConvenience() <= this.max_convenience)
        {
            this.current_convenience += inventory.getConvenience();
            this.folded_inventories.add(inventory);
            return true;
        }
        return false;
    }
    public A_Inventory remove(int index)
    {
        if (index < this.folded_inventories.size() && index >= 0)
        {
            A_Inventory to_return = this.folded_inventories.get(index);
            this.current_convenience -= to_return.getConvenience();
            this.folded_inventories.remove(index);
            return to_return;
        }
        return null;
    }
}
