package Abstract;
import java.util.ArrayList;

public abstract class A_Inventory {

    private double current_mass;
    private double current_size;

    private double max_mass;
    private double max_size;

    private double convenience;
    
    private ArrayList<A_Item> objects;

    public A_Inventory (double max_mass, double max_size, double convenience)
    {
        this.convenience = convenience;
        this.current_mass = 0;
        this.current_size = 0;
        this.max_mass = max_mass;
        this.max_size = max_size;
        this.objects = new ArrayList<A_Item>();
    }

    public double getConvenience()
    {
        return 1/this.convenience;
    }

    public double getMaxMass()
    {
        return this.max_mass;
    }

    public double getMaxSize()
    {
        return this.max_size;
    }

    public boolean append(A_Item some_item)
    {
        this.current_mass = 0;
        this.current_size = 0;

        if (
            this.current_mass + some_item.getMass() <= this.max_mass &&
            this.current_size + some_item.getSize() <= this.max_size
            )
        {
            this.current_mass += some_item.getMass();
            this.current_size += some_item.getSize();
            this.objects.add(some_item);
            return true;
        }
        return false;
    }

    public A_Item remove(int index)
    {
        if (index < this.objects.size() && index >= 0)
        {
            A_Item to_return = this.objects.get(index);
            this.current_mass -= to_return.getMass();
            this.current_size -= to_return.getSize();
            this.objects.remove(index);
            return to_return;
        }
        return null;
    }

    public double getCurrentMass()
    {
        return current_mass;
    }
    public double getCurrentSize()
    {
        return current_size;
    }
}
