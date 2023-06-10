public abstract class A_Item {
    private double mass;
    private double size;

    public A_Item (double mass, double size)
    {
        this.mass = mass;
        this.size = size;
    }
    
    public double getMass()
    {
        return mass;
    }

    public double getSize()
    {
        return size;
    }
}
