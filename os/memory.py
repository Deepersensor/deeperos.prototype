"""
Memory management.
"""

class MemoryManager:
    def __init__(self):
        # Initialize memory management parameters
        self.memory = {}
    
    def allocate(self, process_id, size):
        """Allocate memory for a process."""
        if process_id in self.memory:
            raise Exception("Memory already allocated for this process.")
        self.memory[process_id] = bytearray(size)
    
    def deallocate(self, process_id):
        """Deallocate memory for a process."""
        if process_id not in self.memory:
            raise Exception("No memory allocated for this process.")
        del self.memory[process_id]
    
    def read(self, process_id, address, size):
        """Read memory allocated to a process."""
        if process_id not in self.memory:
            raise Exception("No memory allocated for this process.")
        return bytes(self.memory[process_id][address:address+size])
    
    def write(self, process_id, address, data):
        """Write to memory allocated to a process."""
        if process_id not in self.memory:
            raise Exception("No memory allocated for this process.")
        self.memory[process_id][address:address+len(data)] = data