function barContent() {
    const sections = [
        {
            title: "", links: []
        },
        {
            title: "Giới thiệu",
            links: [["Thông tin chung", "https://soict.hust.edu.vn/category/gioi-thieu"], 
                    ["Triết lý giáo dục", "https://soict.hust.edu.vn/triet-ly-giao-duc"], 
                    ["Cơ cấu tổ chức", "https://soict.hust.edu.vn/co-cau-to-chuc.html"],
                    ["Đảng uỷ - Hội đồng Trường", "https://soict.hust.edu.vn/dang-uy-truong.html"], 
                    ["Ban giám hiệu", "https://soict.hust.edu.vn/ban-giam-hieu.html"],
                    ["Các tổ chức đoàn thể", "https://soict.hust.edu.vn/to-chuc-doan-the.html"], 
                    ["Văn phòng Trường", "https://soict.hust.edu.vn/bo-phan/van-phong-truong"], 
                    ["Danh sách cán bộ", "https://soict.hust.edu.vn/can-bo"]]
        },
        {
            title: "Khoa - Trung tâm",
            links: [["Trung tâm Máy tính và Thực hành", "https://soict.hust.edu.vn/bo-phan/trung-tam-may-tinh-va-thuc-hanh"],
                    ["Trung tâm Đổi mới sáng tạo", "https://soict.hust.edu.vn/bo-phan/trung-tam-doi-moi-sang-tao"], 
                    ["Trung tâm An toàn - An ninh", "https://soict.hust.edu.vn/bo-phan/trung-tam-cyber-security"]]
        },
        {
            title: "Đào tạo",
            links: [["Giới thiệu chung", "https://soict.hust.edu.vn/dao-tao/gioi-thieu-chung"], 
                    ["Hệ đại học", "https://soict.hust.edu.vn/category/dao-tao/he-dai-hoc"], 
                    ["Hệ thạc sỹ", "https://soict.hust.edu.vn/dao-tao/he-thac-sy"], 
                    ["Hệ tiến sỹ", "https://soict.hust.edu.vn/dao-tao/dao-tao-tien-sy"], 
                    ["Đào tạo ngắn hạn", "https://soict.hust.edu.vn/category/dao-tao/dao-tao-ngan-han"]]
        },
        {
            title: "Nghiên cứu",
            links: [["Giới thiệu chung", "https://soict.hust.edu.vn/category/nghien-cuu"], 
                    ["Các Trung tâm nghiên cứu", "https://soict.hust.edu.vn/nghien-cuu/trung-tam-nghien-cuu"], 
                    ["Các Đề tài - Dự án", "https://soict.hust.edu.vn/nghien-cuu/cac-de-tai-du-an"], 
                    ["Công bố khoa học", "https://soict.hust.edu.vn/category/nghien-cuu/cong-bo-khoa-hoc"], 
                    ["Tìm chuyên gia?", "https://soict.hust.edu.vn/can-bo"]]
        },
        {
            title: "Tuyển sinh",
            links: [["Thông tin tuyển sinh 2024", "https://soict.hust.edu.vn/thong-tin-tuyen-sinh-2024.html"], 
                    ["Điểm chuẩn tham khảo", "https://soict.hust.edu.vn/diem-chuan-tham-khao.html"], 
                    ["Hỏi đáp về tuyển sinh", "https://soict.hust.edu.vn/hoi-dap-ve-tuyen-sinh.html"]]
        },
        {
            title: "Sinh viên",
            links: [["Cố vấn học tập", "https://soict.hust.edu.vn/lich-truc-co-van-hoc-tap.html"], 
                    ["Câu lạc bộ Sinh viên", "https://soict.hust.edu.vn/sinh-vien/clbsv"], 
                    ["Thực tập doanh nghiệp", "https://soict.hust.edu.vn/thuc-tap-doanh-nghiep.html"]]
        },
        {
            title: "Hợp tác đối ngoại",
            links: [["Giới thiệu chung", "https://soict.hust.edu.vn/hop-tac-doi-ngoai"], 
                    ["Hợp tác với Khối hàn lâm", "https://soict.hust.edu.vn/hop-tac-quoc-te.html"], 
                    ["Hợp tác với Khối doanh nghiệp", "https://soict.hust.edu.vn/hop-tac-voi-khoi-doanh-nghiep.html"]]
        },
        {
            title: "Cựu sinh viên",
            links: [["Giới thiệu chung", "https://soict.hust.edu.vn/sinh-vien/cuu-sinh-vien"], 
                    ["Tấm gương cựu sinh viên", "https://soict.hust.edu.vn/tam-guong-cuu-sinh-vien.html"]]
        },
        {
            title: "Tin tức - Sự kiện",
            links: [["Thông báo - Tin bài", "https://soict.hust.edu.vn/tin-tuc/thong-bao"], 
                    ["Sự kiện đã diễn ra", "https://soict.hust.edu.vn/su-kien?sort=took-place"], 
                    ["Sự kiện sắp diễn ra", "https://soict.hust.edu.vn/su-kien?sort=upcoming"]]
        },
        {
            title: "Tuyển dụng",
            links: [["Việc làm tại SOICT", "https://soict.hust.edu.vn/tuyen-dung/viec-lam-tai-soict"], 
                    ["Việc làm tại doanh nghiệp", "https://soict.hust.edu.vn/tuyen-dung/viec-lam-cho-sinh-vien"]]
        },
        {
            title: "", links: []
        }
    ];
    
    const container = document.getElementById('bar-container');
    
    sections.forEach(section => {
        const sectionDiv = document.createElement('section');
        sectionDiv.classList.add('bar');
    
        const span = document.createElement('span');
        span.textContent = section.title;
        span.addEventListener('', () => {
            const content = sectionDiv.querySelector('.bar-content');
            content.style.display = content.style.display === 'none' ? 'block' : 'none';
        });
    
        const div = document.createElement('div');
        div.classList.add('bar-content');
    
        section.links.forEach(linkText => {
            const a = document.createElement('a');
            a.href = linkText[1];
            a.textContent = linkText[0];
            div.appendChild(a);
        });
    
        sectionDiv.appendChild(span);
        sectionDiv.appendChild(div);
        container.appendChild(sectionDiv);
    });
}

function newsContent() {
    const newsContents = [
        {
            img: "img/slide-img1.jpg", 
            date: "19/06", 
            content: "Lễ trao chứng nhận Học bổng Khuyến khích học tập kỳ 2023.2", 
            time: "Thời gian: 3:30PM - DD/MM/YY<br>Địa điểm: Hội trường C2 - Online Zoom",
            link: "https://soict.hust.edu.vn/le-trao-chung-nhan-hoc-bong-khuyen-khich-hoc-tap-ky-2023-2.html"
        },
        {
            img: "img/slide-img2.jpg", 
            date: "19/06", 
            content: "Seminar tháng 6/2024 Trường CNTT&TT", 
            time: "Thời gian: 3:30PM - DD/MM/YY<br>Địa điểm: Hội trường C2 - Online Zoom",
            link: "https://soict.hust.edu.vn/seminar-thang-6-2024-truong-cntttt.html"
        },
        {
            img: "img/slide-img3.jpg", 
            date: "15/07", 
            content: "Graduation Day 2024", 
            time: "Thời gian: 3:30PM - DD/MM/YY<br>Địa điểm: Hội trường C2 - Online Zoom",
            link: "https://soict.hust.edu.vn/graduation-day-2024.html"
        },
        {
            img: "img/slide-img4.jpg", 
            date: "24/07", 
            content: "Seminar tháng 7/2024 Trường CNTT&TT", 
            time: "Thời gian: 3:30PM - DD/MM/YY<br>Địa điểm: Hội trường C2 - Online Zoom",
            link: "https://soict.hust.edu.vn/seminar-thang-7-2024-truong-cntttt.html"
        },
        {
            img: "img/slide-img5.jpg", 
            date: "26/07", 
            content: "Tư vấn & Giải đáp Tuyển Sinh", 
            time: "Thời gian: 3:30PM - DD/MM/YY<br>Địa điểm: Hội trường C2 - Online Zoom",
            link: "https://soict.hust.edu.vn/tu-van-giai-dap-tuyen-sinh.html"
        },
        {
            img: "img/slide-img6.jpg", 
            date: "19/08", 
            content: "Trường hè 2024 về Trí tuệ Nhân tạo tạo sinh", 
            time: "Thời gian: 3:30PM - DD/MM/YY<br>Địa điểm: Hội trường C2 - Online Zoom",
            link: "https://soict.hust.edu.vn/truong-he-2024-ve-tri-tue-nhan-tao-tao-sinh.html"
        },
        {
            img: "img/slide-img7.jpg", 
            date: "19/08", 
            content: "2024 Precision Medicine Contest - CryAndRRich", 
            time: "Thời gian: 3:30PM - DD/MM/YY<br>Địa điểm: Hội trường C2 - Online Zoom",
            link: "https://soict.hust.edu.vn/truong-he-ve-y-hoc-chinh-xac-2024-precision-medicine-division-global-project.html"
        },
        {
            img: "img/slide-img8.jpg", 
            date: "19/08", 
            content: "Seminar tháng 8/2024 Trường CNTT&TT", 
            time: "Thời gian: 3:30PM - DD/MM/YY<br>Địa điểm: Hội trường C2 - Online Zoom",
            link: "https://soict.hust.edu.vn/seminar-thang-8-2024-truong-cntttt.html"
        },
        {
            img: "img/slide-img9.jpg", 
            date: "23/09", 
            content: "Seminar tháng 9/2024 Trường CNTT&TT", 
            time: "Thời gian: 3:30PM - DD/MM/YY<br>Địa điểm: Hội trường C2 - Online Zoom",
            link: "https://soict.hust.edu.vn/seminar-thang-9-2024-truong-cntttt.html"
        },
        {
            img: "img/slide-img10.jpg", 
            date: "25/09", 
            content: "Trao chứng chỉ TA cho sinh viên hỗ trợ giảng dạy kỳ 2 năm học 2023-2024", 
            time: "Thời gian: 3:30PM - DD/MM/YY<br>Địa điểm: Hội trường C2 - Online Zoom",
            link: "https://soict.hust.edu.vn/trao-chung-chi-ta-cho-sinh-vien-ho-tro-giang-day-ky-2-nam-hoc-2023-2024.html"
        },
        {
            img: "img/slide-img11.jpg", 
            date: "29/09", 
            content: "Cuộc thi Olympic Tin học BKHN 2024", 
            time: "Thời gian: 3:30PM - DD/MM/YY<br>Địa điểm: Hội trường C2 - Online Zoom",
            link: "https://soict.hust.edu.vn/cuoc-thi-olympic-tin-hoc-bkhn-2024.html"
        },
        {
            img: "img/slide-img12.jpg", 
            date: "13/12", 
            content: "Hội thảo quốc tế về Công nghệ thông tin và truyền thông SOICT", 
            time: "Thời gian: 3:30PM - DD/MM/YY<br>Địa điểm: Hội trường C2 - Online Zoom",
            link: "https://soict.hust.edu.vn/hoi-thao-quoc-te-ve-cong-nghe-thong-tin-va-truyen-thong-soict-2024.html"
        }
    ];

    const container = document.getElementById('slides3');

    newsContents.forEach(contents => {
        const section = document.createElement('section');
        section.classList.add('slide-blocks3');

        const img = document.createElement('img');
        img.classList.add('slide-item3');
        img.src = contents.img;

        const dateP = document.createElement('p');
        dateP.classList.add('date-text');
        dateP.textContent = contents.date;

        const contentP = document.createElement('p');
        contentP.classList.add('content-text');
        contentP.textContent = contents.content;

        const timeP = document.createElement('p');
        timeP.classList.add('time-text');
        timeP.textContent = contents.time;

        const link = document.createElement('a');
        link.href = contents.link;
        link.appendChild(img);

        section.appendChild(link);
        section.appendChild(dateP);
        section.appendChild(contentP);
        section.appendChild(timeP);

        container.appendChild(section);
    });
}

function studentContent() {
    const studentContents = [
        {
            img: "img/exstudent-img1.jpg", 
            content: "Nguyễn Tử Quảng - “Make in Vietnam”: từ BKAV đến BPhone…", 
            quote: "CEO Nguyễn Tử Quảng: ‘Nếu thay đổi định kiến, Việt Nam sẽ là cường quốc công nghệ'",
            link: "https://soict.hust.edu.vn/nguyen-tu-quang.html"
        },
        {
            img: "img/exstudent-img2.jpg", 
            content: "Vương Quang Khải - người đứng sau Zalo và 100 triệu người dùng", 
            quote: "Anh Vương Quang Khải, Cựu sinh viên K41, và hiện là Phó Tổng Giám đốc Tập đoàn VNG",
            link: "https://soict.hust.edu.vn/vuong-quang-khai.html"
        },
        {
            img: "img/exstudent-img3.jpg", 
            content: "Hoàng Việt Anh - Chỉ có một tình yêu duy nhất", 
            quote: "Tổng giám đốc FPT Software Hoàng Việt Anh đã gắn bó với FPT Software hơn 20 năm",
            link: "https://soict.hust.edu.vn/hoang-viet-anh-chi-co-mot-tinh-yeu-duy-nhat.html"
        },
        {
            img: "img/exstudent-img4.jpg", 
            content: "Lữ Thành Long - Thủ lĩnh công nghệ", 
            quote: "Cựu sinh viên K34, Chủ tịch HĐQT Công ty Cổ phần MISA",
            link: "https://soict.hust.edu.vn/lu-thanh-long-thu-linh-cong-nghe.html"
        },
        {
            img: "img/exstudent-img5.jpg", 
            content: "Nguyễn Hà Đông - Cha đẻ Flappy Bird “náo loạn” Thế giới", 
            quote: "“Flappy Guy” cho rằng mình phải đánh đổi một số thứ để đạt được thành công",
            link: "https://soict.hust.edu.vn/nguyen-ha-dong.html"
        },
        {
            img: "img/exstudent-img6.jpg", 
            content: "Hùng Trần - Tấm gương khởi nghiệp người Việt tại Silicon Valley", 
            quote: "Cựu nghiên cứu sinh Quỹ Giáo dục Việt Nam (VEF) ngành Khoa học Máy tính, Đại học Iowa (Mỹ)",
            link: "https://soict.hust.edu.vn/tran-viet-hung.html"
        }
    ];

    const container = document.getElementById('slides4');

    studentContents.forEach(contents => {
        const section = document.createElement('section');
        section.classList.add('slide-blocks4');

        const img = document.createElement('img');
        img.classList.add('slide-item4');
        img.src = contents.img;

        const exStudent = document.createElement('p');
        exStudent.id = 'ex';
        exStudent.textContent = 'Cựu Sinh viên';

        const contentP = document.createElement('p');
        contentP.classList.add('content-text');
        contentP.textContent = contents.content;

        const quoteP = document.createElement('p');
        quoteP.classList.add('quote-text');
        quoteP.textContent = contents.quote;

        const link = document.createElement('a');
        link.href = contents.link;
        link.appendChild(img);

        section.appendChild(link);
        section.appendChild(exStudent);
        section.appendChild(contentP);
        section.appendChild(quoteP);

        container.appendChild(section);
    });

}

function slideImage(imagePerView, move) {
    const slides = document.querySelector('.slides' + imagePerView);
    const slide = document.querySelectorAll('.slide-item' + imagePerView);
    let currentIndex = 0;
    console.log(slides);

    document.getElementById('next'+ imagePerView).addEventListener('click', () => {
        if (currentIndex < slide.length - imagePerView) {
            currentIndex++;
        }
        else {
            currentIndex = 0;
        }
        slides.style.transform = `translateX(-${currentIndex * move}vw)`;
    });
    
    document.getElementById('prev'+ imagePerView).addEventListener('click', () => {
        if (currentIndex > 0) {
            currentIndex--;
        }
        else {
            currentIndex = slide.length - imagePerView;
        }
        slides.style.transform = `translateX(-${currentIndex * move}vw)`;
    });
}

function showImage(index) {
    const images = document.querySelectorAll('.soict-img');
    const texts = document.querySelectorAll('.soict-text');
    const buttons = document.querySelectorAll('.soict-button');
    const names = document.querySelectorAll('.soict-name');
    images.forEach((img, i) => {
        img.classList.remove('active');
        texts[i].classList.remove('active');
        buttons[i].classList.remove('active');
        names[i].classList.remove('active');
    });
    document.getElementById('img' + index).classList.add('active');
    document.getElementById('soict-text' + index).classList.add('active');
    document.getElementById('soict-button' + index).classList.add('active');
    document.getElementById('name' + index).classList.add('active');
}
