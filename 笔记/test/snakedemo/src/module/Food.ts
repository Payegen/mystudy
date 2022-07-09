class Food{

    food:HTMLElement;

    constructor(){
        this.food = document.getElementById('id')!;
    }

    get X(){
        return this.food.offsetLeft
    }
    get Y(){
        return this.food.offsetTop
    }

}
export default Food;