class LRUCache {
    private int capacity;
    private HashMap<Integer, Integer> cache;
    private ArrayList<Integer> stack;

    public LRUCache(int capacity) {
        this.capacity = capacity;
        this.cache = new HashMap<>();
        this.stack = new ArrayList<>();
    }
    
    public int get(int key) {
        if (!cache.containsKey(key)){
            return -1;
        }
        else {
            stack.remove(Integer.valueOf(key));
            stack.add(key);
            return cache.get(key);
        }
    }
    
    public void put(int key, int value) {
        if (cache.containsKey(key)){
            cache.put(key, value);
            stack.remove(Integer.valueOf(key));
            stack.add(key);
        }
        else{
            if (cache.size() < capacity){
                cache.put(key, value);
                stack.add(key);
            }
            else{
                int lru_key = stack.remove(0);
                cache.remove(lru_key);

                cache.put(key, value);
                stack.add(key);
            }
        }
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */