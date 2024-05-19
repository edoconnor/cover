import tkinter as tk

class RectangleCoverageApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Rectangle Coverage Checker")
        self.canvas = tk.Canvas(self, width=500, height=500, bg='white')
        self.canvas.pack(padx=10, pady=10)

        self.btn_set_target = tk.Button(self, text="Set Target", command=self.set_target_mode)
        self.btn_set_target.pack(side=tk.LEFT, padx=(10, 2))

        self.btn_set_region = tk.Button(self, text="Set Region", command=self.set_region_mode)
        self.btn_set_region.pack(side=tk.LEFT, padx=(2, 10))

        self.btn_check_coverage = tk.Button(self, text="Check Coverage", command=self.check_coverage)
        self.btn_check_coverage.pack(side=tk.LEFT, padx=(2, 10))

        self.btn_clear = tk.Button(self, text="Clear", command=self.clear_canvas)
        self.btn_clear.pack(side=tk.LEFT, padx=(2, 10))

        self.label_result = tk.Label(self, text="Result: None", bg='lightgrey', width=20)
        self.label_result.pack(side=tk.LEFT, padx=(2, 10))

        self.target = None
        self.regions = []
        self.canvas.bind("<Button-1>", self.on_mouse_down)
        self.canvas.bind("<B1-Motion>", self.on_mouse_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_mouse_release)

        self.mode = None 

    def set_target_mode(self):
        self.mode = 'target'
        self.label_result.config(text="Mode: Setting Target")
        print("Mode set to target.")

    def set_region_mode(self):
        self.mode = 'region'
        self.label_result.config(text="Mode: Adding Regions")
        print("Mode set to region.")

    def on_mouse_down(self, event):
        self.start_x = event.x
        self.start_y = event.y
        self.rect = self.canvas.create_rectangle(self.start_x, self.start_y, event.x, event.y, outline='black')
        print(f"Start drawing rectangle at ({self.start_x}, {self.start_y})")

    def on_mouse_drag(self, event):
        self.canvas.coords(self.rect, self.start_x, self.start_y, event.x, event.y)
        print(f"Resizing rectangle to ({event.x}, {event.y})")

    def on_mouse_release(self, event):
        final_rect = (min(self.start_x, event.x), min(self.start_y, event.y), max(self.start_x, event.x), max(self.start_y, event.y))
        print(f"Rectangle finalized at {final_rect}")
        if self.mode == 'target':
            if self.target:
                self.canvas.delete(self.target[0])  
            self.target = (self.rect, final_rect)
            self.canvas.itemconfig(self.rect, outline='red')
            print("Target set.")
        elif self.mode == 'region':
            self.regions.append((self.rect, final_rect))
            self.canvas.itemconfig(self.rect, outline='blue')
            print("Region added.")

    def check_coverage(self):
        if not self.target or not self.regions:
            self.label_result.config(text="Set target & regions first")
            print("Coverage check failed: Target or regions not properly set.")
            return
        print("Checking coverage...")
        covered = self.is_covered(self.target[1], [r[1] for r in self.regions])
        self.label_result.config(text=f"Covered: {covered}")
        print(f"Coverage result: {covered}")

    def is_covered(self, target, regions):
        tx1, ty1, tx2, ty2 = min(target[0], target[2]), min(target[1], target[3]), max(target[0], target[2]), max(target[1], target[3])
        target_corners = [(tx1, ty1), (tx2, ty1), (tx1, ty2), (tx2, ty2)]
        for corner in target_corners:
            if not any(self.point_in_rectangle(corner, rect) for rect in regions):
                print(f"Corner {corner} is not covered.")
                return False
        return True

    def point_in_rectangle(self, point, rect):
        px, py = point
        rx1, ry1, rx2, ry2 = min(rect[0], rect[2]), min(rect[1], rect[3]), max(rect[0], rect[2]), max(rect[1], rect[3])
        result = rx1 <= px <= rx2 and ry1 <= py <= ry2
        if result:
            print(f"Point {point} is within rectangle {rect}")
        else:
            print(f"Point {point} is not within rectangle {rect}")
        return result

    def clear_canvas(self):
        self.canvas.delete("all")
        self.target = None
        self.regions = []
        self.label_result.config(text="Result: None")
        print("Canvas cleared.")

if __name__ == "__main__":
    app = RectangleCoverageApp()
    app.mainloop()
