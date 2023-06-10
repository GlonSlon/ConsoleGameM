import java.util.ArrayList;

public abstract class A_Inventory {

    private double current_mass;
    private double current_size;

    private double max_mass;
    private double max_size;
    
    private ArrayList<A_Item> objects;

    public A_Inventory (double max_mass, double max_size)
    {
        this.current_mass = 0;
        this.current_size = 0;
        this.max_mass = max_mass;
        this.max_size = max_size;
        this.objects = new ArrayList<A_Item>();
    }

    public double getMaxMass()
    {
        return max_mass;
    }

    public double getMaxSize()
    {
        return max_size;
    }

    public boolean append(A_Item some_object)
    {
        this.current_mass = 0;
        this.current_size = 0;

        for(A_Item elem: this.objects)
        {   
            this.current_mass += elem.getMass();
            this.current_size += elem.getSize();
        }
        if (
            this.current_mass + some_object.getMass() <= this.max_mass &&
            this.current_size + some_object.getSize() <= this.max_size
            )
        {
            this.objects.add(some_object);
            return true;
        }
        return false;
    }

    public boolean remove(int index)
    {
        if (index < this.objects.size() && index >= 0)
        {
            this.objects.remove(index);
            return true;
        }
        return false;
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
