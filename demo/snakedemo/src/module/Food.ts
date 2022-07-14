class Food{

    private food:HTMLElement;

    constructor(){
        this.food = document.getElementById('food')!;
    }

    get X(){
        return this.food.offsetLeft
    }
    get Y(){
        return this.food.offsetTop
    }

    set X(value){
        this.food.style.left = value + 'px'
    }
    set Y(value){
        this.food.style.top = value + 'px'
    }

    change(){
        let top = Math.round(Math.random() * 29) * 10;
        let left = Math.round(Math.random() * 29) * 10;

        this.food.style.left = left + 'px';
        this.food.style.top = top + 'px';
    }
}
export default Food;